from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
import uuid


class Exercise(models.Model):
    """
    Stores a single exercise in a plan.
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    sets = models.PositiveIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(20))
    )
    reps = models.PositiveIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(50))
    )
    load = models.PositiveIntegerField()
    comment = models.CharField(max_length=255)


class Training(models.Model):
    """
    Stores information about the training and the exercises in it.
    Related to :model:`trainer_app.trainingplan` and :model:`trainer_app.exercise`
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise, through="ExerciseTraining")


class DayName(models.Model):
    """
    Represents the name of a day of the week. Is used in ExerciseTraining
    to show which day does the training happen.
    """

    Days = (
        "Poniedziałek",
        "Wtorek",
        "Środa",
        "Czwartek",
        "Piątek",
        "Sobota",
        "Niedziela",
    )
    name = models.CharField(
        choices=list(enumerate(Days, start=1)), max_length=32, default=1
    )


class ExerciseTraining(models.Model):
    """
    Model that contains information about relation between :model:`trainer_app.training` and
    :model:`trainer_app.exercise`.
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)


class TrainingPlan(models.Model):
    """
    Stores a single training plan. Relations to :model:`auth.user` and :model:`trainer_app.training`
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    trainings = models.ForeignKey(Training, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
