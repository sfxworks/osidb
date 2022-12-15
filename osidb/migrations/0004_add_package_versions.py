# Generated by Django 3.2.8 on 2021-10-21 05:58

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("osidb", "0003_auto_20211019_0839"),
    ]

    operations = [
        migrations.CreateModel(
            name="PackageVersions",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "acl_read",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.UUIDField(), default=list, size=None
                    ),
                ),
                (
                    "acl_write",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.UUIDField(), default=list, size=None
                    ),
                ),
            ],
            options={
                "verbose_name": "Package Versions",
            },
        ),
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "acl_read",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.UUIDField(), default=list, size=None
                    ),
                ),
                (
                    "acl_write",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.UUIDField(), default=list, size=None
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_osidb.version_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Version",
            },
        ),
        migrations.RemoveField(
            model_name="flaw",
            name="package",
        ),
        migrations.RemoveField(
            model_name="flawevent",
            name="package",
        ),
        migrations.RemoveField(
            model_name="flawhistory",
            name="package",
        ),
        migrations.CreateModel(
            name="CVEv5PackageVersions",
            fields=[
                (
                    "packageversions_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="osidb.packageversions",
                    ),
                ),
                ("package", models.CharField(max_length=2058)),
                (
                    "default_status",
                    models.CharField(
                        choices=[
                            ("AFFECTED", "Affected"),
                            ("UNAFFECTED", "Unaffected"),
                            ("UNKNOWN", "Unknown"),
                        ],
                        default="UNAFFECTED",
                        max_length=1024,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("osidb.packageversions",),
        ),
        migrations.CreateModel(
            name="CVEv5Version",
            fields=[
                (
                    "version_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="osidb.version",
                    ),
                ),
                ("version", models.CharField(max_length=1024)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("AFFECTED", "Affected"),
                            ("UNAFFECTED", "Unaffected"),
                            ("UNKNOWN", "Unknown"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("osidb.version",),
        ),
        migrations.AddField(
            model_name="packageversions",
            name="flaw",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="package_versions",
                to="osidb.flaw",
            ),
        ),
        migrations.AddField(
            model_name="packageversions",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_osidb.packageversions_set+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="packageversions",
            name="versions",
            field=models.ManyToManyField(to="osidb.Version"),
        ),
    ]