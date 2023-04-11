# Generated by Django 3.2.15 on 2023-03-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osidb', '0069_flaw_component'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flaw',
            name='resolution',
            field=models.CharField(blank=True, choices=[('', 'Novalue'), ('DUPLICATE', 'Duplicate'), ('WONTFIX', 'Wontfix'), ('NOTABUG', 'Notabug'), ('ERRATA', 'Errata'), ('CANTFIX', 'Cantfix'), ('DEFERRED', 'Deferred'), ('CURRENTRELEASE', 'Currentrelease'), ('UPSTREAM', 'Upstream'), ('RAWHIDE', 'Rawhide'), ('INSUFFICIENT_DATA', 'Insufficient Data'), ('NEXTRELEASE', 'Nextrelease'), ('WORKSFORME', 'Worksforme'), ('EOL', 'Eol')], default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flaw',
            name='state',
            field=models.CharField(choices=[('ASSIGNED', 'Assigned'), ('CLOSED', 'Closed'), ('MODIFIED', 'Modified'), ('NEW', 'New'), ('ON_DEV', 'On Dev'), ('ON_QA', 'On Qa'), ('POST', 'Post'), ('RELEASE_PENDING', 'Release Pending'), ('VERIFIED', 'Verified')], default='NEW', max_length=100, null=True),
        ),
    ]