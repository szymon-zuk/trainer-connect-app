# Generated by Django 4.2.1 on 2023-06-02 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0004_alter_thread_trainee_id_alter_thread_trainer_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thread",
            name="trainee_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trainee_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="thread",
            name="trainer_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trainer_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]