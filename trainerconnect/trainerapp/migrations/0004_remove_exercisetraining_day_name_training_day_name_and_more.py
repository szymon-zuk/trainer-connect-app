# Generated by Django 4.2.1 on 2023-05-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trainerapp", "0003_exercisetraining_training_trainingplan_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exercisetraining",
            name="day_name",
        ),
        migrations.AddField(
            model_name="training",
            name="day_name",
            field=models.CharField(
                choices=[
                    ("Pn", "Poniedziałek"),
                    ("Wt", "Wtorek"),
                    ("Śr", "Środa"),
                    ("Czw", "Czwartek"),
                    ("Pt", "Piątek"),
                    ("Sob", "Sobota"),
                    ("Ndz", "Niedziela"),
                ],
                default="Pn",
            ),
        ),
        migrations.DeleteModel(
            name="DayName",
        ),
    ]
