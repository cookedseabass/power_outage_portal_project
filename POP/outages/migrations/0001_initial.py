# Generated by Django 5.0.7 on 2024-07-29 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OutageReport",
            fields=[
                ("report_id", models.AutoField(primary_key=True, serialize=False)),
                ("report_date", models.DateTimeField(auto_now_add=True)),
                ("location", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("status", models.CharField(max_length=50)),
                ("planned", models.BooleanField(default=False)),
                ("estimates_restoration_time", models.DateTimeField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
    ]
