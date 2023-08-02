from .models import Message, Thread
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_thread_list_view_requires_login(user, client):
    response = client.get("/thread_list/")
    assert response.status_code == 302
    assert response.url == "/login/?next=/thread_list/"
    client.force_login(user=user)
    response = client.get("/thread_list/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_thread_list_view(user, client):
    client.force_login(user=user)
    response = client.get("/thread_list/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_thread_view_requires_login(user, client):
    response = client.get("/add_thread/")
    assert response.status_code == 302
    assert response.url == "/login/?next=/add_thread/"
    client.force_login(user=user)
    response = client.get("/add_thread/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_thread_view(user, client):
    client.force_login(user=user)
    response = client.get("/add_thread/")
    assert response.status_code == 200
    initial_thread_count = Thread.objects.count()
    response = client.post(
        "/add_thread/",
        {
            "name": "Testowa konwersacja",
            "trainer_id": user.id,
            "trainee_id": user.id,
            "description": "Opis konwersacji",
        },
    )
    assert response.status_code == 302
    assert Thread.objects.count() == initial_thread_count + 1


@pytest.mark.django_db
def test_add_message_view_requires_login(user, client):
    response = client.get("/add_message/")
    assert response.status_code == 302
    assert response.url == "/login/?next=/add_message/"
    client.force_login(user=user)
    response = client.get("/add_message/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_message_view(user, client, thread, current_date):
    client.force_login(user=user)
    response = client.get("/add_message/")
    assert response.status_code == 200
    initial_message_count = Message.objects.count()
    response = client.post(
        "/add_message/",
        {
            "username": "Nazwa użytkownika",
            "text": "tekst wiadomości",
            "created": "2023-05-24 17:40:06.476497 +00:00",
            "thread": thread.id,
        },
    )
    assert response.status_code == 302
    assert Message.objects.count() == initial_message_count + 1


@pytest.mark.django_db
def test_thread_detail_view_requires_login(user, client, thread):
    response = client.get(reverse("thread", kwargs={"pk": thread.id}))
    assert response.status_code == 302
    client.force_login(user=user)
    response = client.get(reverse("thread", kwargs={"pk": thread.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_thread_detail_view(user, client, thread):
    client.force_login(user=user)
    response = client.get(reverse("thread", kwargs={"pk": thread.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_message_view_requires_login(user, client, message):
    response = client.get(reverse("delete-message", kwargs={"pk": message.id}))
    assert response.status_code == 302
    client.force_login(user=user)
    response = client.post(reverse("delete-message", kwargs={"pk": message.id}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_message_view(user, client, message):
    client.force_login(user=user)
    response = client.get(reverse("delete-message", kwargs={"pk": message.id}))
    assert response.status_code == 200
    initial_message_count = Message.objects.count()
    response = client.post(reverse("delete-message", kwargs={"pk": message.id}))
    assert response.status_code == 302
    assert Message.objects.count() == initial_message_count - 1


@pytest.mark.django_db
def test_delete_thread_view_requires_login(user, client, thread):
    response = client.get(reverse("delete-thread", kwargs={"pk": thread.id}))
    assert response.status_code == 302
    client.force_login(user=user)
    response = client.post(reverse("delete-thread", kwargs={"pk": thread.id}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_thread_view(user, client, thread):
    client.force_login(user=user)
    response = client.get(reverse("delete-thread", kwargs={"pk": thread.id}))
    assert response.status_code == 200
    initial_thread_count = Thread.objects.count()
    response = client.post(reverse("delete-thread", kwargs={"pk": thread.id}))
    assert response.status_code == 302
    assert Thread.objects.count() == initial_thread_count - 1
