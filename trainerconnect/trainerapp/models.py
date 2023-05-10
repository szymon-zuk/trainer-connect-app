from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class Exercise(models.Model):
    name = models.CharField(max_length=32)
    sets = models.PositiveIntegerField(validators=(MinValueValidator(1), MaxValueValidator(20)))
    reps = models.PositiveIntegerField(validators=(MinValueValidator(1), MaxValueValidator(50)))
    load = models.PositiveIntegerField()
    comment = models.CharField(max_length=255)


class DayName(models.Model):
    Days = (
        'Poniedziałek',
        'Wtorek',
        'Środa',
        'Czwartek',
        'Piątek',
        'Sobota',
        'Niedziela'
    )
    name = models.CharField(choices=list(enumerate(Days, start=1)), max_length=32, default=1)

