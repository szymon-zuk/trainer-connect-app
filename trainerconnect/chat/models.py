from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Thread(models.Model):
    """A thread between 2 people - a trainer and his trainee"""

    name = models.CharField(max_length=64)
    trainer_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trainer_id"
    )
    trainee_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trainee_id"
    )
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Message(models.Model):
    """Model that represents a single message in a thread"""

    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text[:30]
