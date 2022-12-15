# Generated by Django 3.2.13 on 2022-04-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("osidb", "0040_flawcomment_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flaw",
            name="state",
            field=models.CharField(
                choices=[
                    ("ASSIGNED", "Assigned"),
                    ("CLOSED", "Closed"),
                    ("MODIFIED", "Modified"),
                    ("NEW", "New"),
                    ("ON_DEV", "On Dev"),
                    ("ON_QA", "On Qa"),
                    ("POST", "Post"),
                    ("RELEASE_PENDING", "Release Pending"),
                    ("VERIFIED", "Verified"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="flawevent",
            name="state",
            field=models.CharField(
                choices=[
                    ("ASSIGNED", "Assigned"),
                    ("CLOSED", "Closed"),
                    ("MODIFIED", "Modified"),
                    ("NEW", "New"),
                    ("ON_DEV", "On Dev"),
                    ("ON_QA", "On Qa"),
                    ("POST", "Post"),
                    ("RELEASE_PENDING", "Release Pending"),
                    ("VERIFIED", "Verified"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="flawhistory",
            name="state",
            field=models.CharField(
                choices=[
                    ("ASSIGNED", "Assigned"),
                    ("CLOSED", "Closed"),
                    ("MODIFIED", "Modified"),
                    ("NEW", "New"),
                    ("ON_DEV", "On Dev"),
                    ("ON_QA", "On Qa"),
                    ("POST", "Post"),
                    ("RELEASE_PENDING", "Release Pending"),
                    ("VERIFIED", "Verified"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]