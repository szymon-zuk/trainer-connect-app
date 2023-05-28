from django.contrib.auth.models import User
import pytest
from django.test import Client
from .models import Exercise, Training, TrainingPlan


@pytest.fixture
def user():
    user = User.objects.create_user(id=1, username="user", password="")
    return user


@pytest.fixture
def client():
    c = Client()
    return c


@pytest.fixture
def exercise():
    e = Exercise.objects.create(
        name="Wyciskanie leżąc",
        sets=5,
        reps=5,
        load=100,
        comment="szeroki chwyt"
    )
    return e


@pytest.fixture
def training(exercise):
    t = Training.objects.create(
    name="Trening nóg",
    description="Poniedziałek, duża intensywność"
    )
    t.exercises.add(exercise)
    t.refresh_from_db()
    return t


@pytest.fixture
def training_plan(user, training):
    p = TrainingPlan.objects.create(
        name="Nowy plan",
        description="opis treningu",
        user_id=user
    )
    p.trainings.add(training)
    p.refresh_from_db()
    return p
