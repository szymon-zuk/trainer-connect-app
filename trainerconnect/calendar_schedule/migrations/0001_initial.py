# Generated by Django 4.2.1 on 2023-05-29 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=64, null=True, verbose_name="Title"),
                ),
                (
                    "start",
                    models.DateTimeField(
                        default=datetime.datetime.now,
                        null=True,
                        verbose_name="Start date",
                    ),
                ),
                (
                    "end",
                    models.DateTimeField(
                        default=datetime.datetime.now,
                        null=True,
                        verbose_name="End date",
                    ),
                ),
                (
                    "host_email",
                    models.EmailField(default="szymon.p.zuk@gmail.com", max_length=254),
                ),
                ("guest_email", models.EmailField(max_length=254)),
                ("location", models.CharField(max_length=64)),
                ("event_description", models.CharField(max_length=100)),
                (
                    "event_id",
                    models.CharField(
                        max_length=1024, null=True, verbose_name="Event id"
                    ),
                ),
            ],
        ),
    ]