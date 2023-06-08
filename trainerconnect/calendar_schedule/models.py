from django.db import models

# Create your models here.
from datetime import datetime


class Event(models.Model):
    title = models.CharField("Title", max_length=64, null=True)
    start = models.DateTimeField("Start date", default=datetime.now, null=True)
    end = models.DateTimeField("End date", default=datetime.now, null=True)
    location = models.CharField(max_length=64)
    event_description = models.CharField(max_length=100)
    event_id = models.CharField("Event id", max_length=1024, null=True)

    def __str__(self):
        return self.title
