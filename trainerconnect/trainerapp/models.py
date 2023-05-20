from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
import uuid


class Exercise(models.Model):
    """
    Stores a single exercise in a plan.
    """

    name = models.CharField(max_length=32)
    sets = models.PositiveIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(20))
    )
    reps = models.PositiveIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(50))
    )
    load = models.PositiveIntegerField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Training(models.Model):
    """
    Stores information about the training and the exercises in it.
    Related to :model:`trainer_app.trainingplan` and :model:`trainer_app.exercise`
    """

    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    days = (
        ("Pn", "Poniedziałek"),
        ("Wt", "Wtorek"),
        ("Śr", "Środa"),
        ("Czw", "Czwartek"),
        ("Pt", "Piątek"),
        ("Sob", "Sobota"),
        ("Ndz", "Niedziela"),
    )
    day_name = models.CharField(default="Pn", choices=days)
    exercises = models.ManyToManyField(Exercise, through="ExerciseTraining", blank=True)

    def __str__(self):
        return self.name


class ExerciseTraining(models.Model):
    """
    Model that contains information about relation between :model:`trainer_app.training` and
    :model:`trainer_app.exercise`.
    """

    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)


class TrainingPlan(models.Model):
    """
    Stores a single training plan. Relations to :model:`auth.user` and :model:`trainer_app.training`
    """

    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    trainings = models.ForeignKey(Training, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
