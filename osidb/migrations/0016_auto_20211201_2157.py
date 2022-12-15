# Generated by Django 3.2.9 on 2021-12-01 21:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("osidb", "0015_auto_20211201_2027"),
    ]

    operations = [
        migrations.AddField(
            model_name="affect",
            name="created_dt",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="affect",
            name="updated_dt",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="affectevent",
            name="created_dt",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="affectevent",
            name="updated_dt",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="tracker",
            name="created_dt",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tracker",
            name="updated_dt",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="trackerevent",
            name="created_dt",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="trackerevent",
            name="updated_dt",
            field=models.DateTimeField(auto_now=True),
        ),
    ]