# Generated by Django 4.2.1 on 2023-05-31 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_remove_message_thread_thread_messages"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="thread",
            name="messages",
        ),
        migrations.AddField(
            model_name="message",
            name="thread",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="chat.thread"
            ),
        ),
    ]
