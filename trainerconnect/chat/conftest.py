from django.contrib.auth.models import User
import pytest
from django.test import Client
from .models import Thread, Message


@pytest.fixture
def user():
    user = User.objects.create_user(username="user", password="")
    return user


@pytest.fixture
def client():
    c = Client()
    return c


@pytest.fixture
def thread():
    t = Thread.objects.create(
        name="Konwersacja testowa", 
        trainer_id=user.id, 
        trainee_id=user.id, 
        description="Opis testowy"
    )
    return t


@pytest.fixture
def message(thread):
    m = Message.objects.create(
        username="Szymson", 
        text="tekst wiadomości"
    )
    m.thread.add(thread)
    m.refresh_from_db()
    return m
