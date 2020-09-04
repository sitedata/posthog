# Generated by Django 3.0.7 on 2020-09-03 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0083_auto_20200826_1504"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="current_team",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="posthog.Team"),
        ),
    ]