from django.contrib.auth.models import User
import pytest
from django.test import Client
from .models import Thread, Message
from django.contrib.auth import get_user_model
from datetime import datetime


@pytest.fixture
def user():
    user = User.objects.create_user(id=1, username="user", password="")
    return user


@pytest.fixture
def user2():
    user2 = User.objects.create_user(id=2, username="user2", password="")
    return user2


@pytest.fixture
def client():
    c = Client()
    return c


@pytest.fixture
def thread(user, user2):
    t = Thread.objects.create(
        name="Konwersacja testowa",
        description="Opis testowy",
        trainer_id=user,
        trainee_id=user2,
    )
    return t


@pytest.fixture
def message(user, thread):
    m = Message.objects.create(username=user, text="tekst wiadomości", thread=thread)
    m.refresh_from_db()
    return m


@pytest.fixture(autouse=True)
def current_date():
    return datetime(2023, 6, 2, 0, 0, 0)
