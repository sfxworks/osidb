from datetime import datetime

from django.utils.timezone import make_aware

from collectors.bzimport.collectors import BugzillaQuerier
from osidb.constants import DATETIME_FMT
from osidb.exceptions import DataInconsistencyException
from osidb.models import Flaw

from .exceptions import UnsaveableFlawError
from .query import FlawBugzillaQueryBuilder


class BugzillaSaver(BugzillaQuerier):
    """
    Bugzilla bug save handler underlying model instance
    the instance validity is assumed and not checked
    """

    @property
    def model(self):
        """
        instance model class getter
        needs to be defined in the subclasses
        """
        raise NotImplementedError

    @property
    def query_builder(self):
        """
        query builder class getter
        needs to be defined in the subclasses
        """
        raise NotImplementedError

    def __init__(self, instance, bz_api_key):
        """
        init stuff
        """
        self.instance = instance
        # substitute the default service Bugzilla API key
        # so the resulting Bugzilla audit log corresponds
        # to the acutal user requesting the operation
        self._bz_api_key = bz_api_key

    def save(self):
        """
        generic save serving as class entry point
        which calls create or update handler to continue
        returns an updated instance (without saving)
        """
        return self.create() if self.instance.bz_id is None else self.update()

    def create(self):
        """
        create a bug underlying the model instance in Bugilla
        """
        bugzilla_query_builder = self.query_builder(self.instance)
        response = self.bz_conn.createbug(bugzilla_query_builder.query)
        self.instance.bz_id = response.id
        return self.instance

    def update(self):
        """
        update a bug underlying the model instance in Bugilla
        """
        old_instance = self.model.objects.get(uuid=self.instance.uuid)
        bugzilla_query_builder = self.query_builder(self.instance, old_instance)
        self.check_collisions()  # check for collisions right before the update
        self.bz_conn.update_bugs([self.instance.bz_id], bugzilla_query_builder.query)
        return self.instance

    def check_collisions(self):
        """
        one last preventative check that Bugzilla last_change_time
        really corresponds to the stored one so there was no collision
        """
        if self.actual_last_chante != self.stored_last_change:
            raise DataInconsistencyException(
                "Save operation based on an outdated model instance"
            )

    @property
    def actual_last_chante(self):
        """
        retrieve the actual last change timestamp from Bugzilla
        """
        return make_aware(
            datetime.strptime(
                self.get_bug_data(
                    self.instance.bz_id, include_fields=["last_change_time"]
                )["last_change_time"],
                DATETIME_FMT,
            )
        )

    @property
    def stored_last_change(self):
        """
        retrive the stored last change timestamp from DB
        """
        return make_aware(
            datetime.strptime(self.instance.meta_attr["last_change_time"], DATETIME_FMT)
        )


class FlawBugzillaSaver(BugzillaSaver):
    """
    Bugzilla flaw bug save handler
    """

    @property
    def flaw(self):
        """
        concrete name shortcut
        """
        return self.instance

    @property
    def model(self):
        """
        instance model class getter
        """
        return Flaw

    @property
    def query_builder(self):
        """
        query builder class getter
        """
        return FlawBugzillaQueryBuilder

    def update(self):
        """
        update flaw in Bugzilla
        """
        # TODO flaws with multiple CVEs introduce a paradox behavior
        # when modifying a flaw the way that the CVE ID is removed as
        # in OSIDB it basically results in a flaw removal
        # so let us restrict it for now - should be rare
        if (
            self.model.objects.filter(meta_attr__bz_id=self.flaw.bz_id).count() > 1
            and not self.flaw.cve_id
        ):
            raise UnsaveableFlawError(
                "Unable to remove a CVE ID from a flaw with multiple CVEs "
                "due to an ambigous N to 1 OSIDB to Buzilla flaw mapping"
            )

        return super().update()
