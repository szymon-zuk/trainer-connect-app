from django.test import Client
from . models import Exercise, Training, TrainingPlan
import pytest
from django.urls import reverse


def test_main():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200


def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_exercise_view_requires_login(user, client):
    response = client.get('/add_exercise/')
    assert response.status_code == 302
    assert response.url == '/login/?next=/add_exercise/'
    client.force_login(user=user)
    response = client.get('/add_exercise/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_exercise_list_view_requires_login(user, client):
    response = client.get(reverse("exercise-list"))
    assert response.status_code == 302
    assert response.url == '/login/?/exercise_list/=/exercise_list/'
    client.force_login(user=user)
    response = client.get(reverse("exercise-list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_exercise_view_requires_login(user, client, exercise):
    response = client.get(reverse("update-exercise", kwargs={"pk": exercise.id}))
    assert response.status_code == 302
    client.force_login(user=user)
    response = client.post(reverse("update-exercise", kwargs={"pk": exercise.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_exercise_view(user, client):
    client.force_login(user=user)
    response = client.get('/add_exercise/')
    assert response.status_code == 200
    initial_exercise_count = Exercise.objects.count()
    response = client.post('/add_exercise/', {
        "name": "Nowe ćwiczenie",
        "sets": 5,
        "reps": 5,
        "load": 100,
        "comment": "Nowy komentarz"
    })
    assert response.status_code == 302
    assert Exercise.objects.count() == initial_exercise_count + 1


@pytest.mark.django_db
def test_delete_exercise_view(user, client, exercise):
    client.force_login(user=user)
    response = client.get(reverse("delete-exercise", kwargs={"pk": exercise.id}))
    assert response.status_code == 200
    initial_exercise_count = Exercise.objects.count()
    response = client.post(reverse("delete-exercise", kwargs={"pk": exercise.id}))
    assert response.status_code == 302
    assert Exercise.objects.count() == initial_exercise_count - 1


@pytest.mark.django_db
def test_exercise_list_view(user, client):
    client.force_login(user=user)
    response = client.get('/exercise_list/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_exercise_view(user, client, exercise):
    client.force_login(user=user)
    response = client.get(reverse("update-exercise", kwargs={"pk": exercise.id}))
    assert response.status_code == 200
    payload = {
        "name": "Update ćwiczenia",
        "sets": 6,
        "reps": 6,
        "load": 120,
        "comment": "Nowszy komentarz"
    }
    response = client.post(reverse("update-exercise", kwargs={"pk": exercise.id}), data=payload)
    assert response.status_code == 302
    exercise.refresh_from_db()
    assert exercise.name == payload['name']
    assert exercise.sets == payload['sets']
    assert exercise.reps == payload['reps']
    assert exercise.load == payload['load']
    assert exercise.comment == payload['comment']


@pytest.mark.django_db
def test_add_training_view_requires_login(user, client):
    response = client.get('/add_training/')
    assert response.status_code == 302
    assert response.url == '/login/?/add_training/=/add_training/'
    client.force_login(user=user)
    response = client.get('/add_training/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_training_list_view_requires_login(user, client):
    response = client.get('/training_list/')
    assert response.status_code == 302
    assert response.url == '/login/?/training_list/=/training_list/'
    client.force_login(user=user)
    response = client.get('/training_list/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_training_view_requires_login(user, client, training):
    response = client.get(reverse("update-training", kwargs={"pk": training.id}))
    assert response.status_code == 302
    client.force_login(user=user)
    response = client.post(reverse("update-training", kwargs={"pk": training.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_training_view(user, client, exercise):
    client.force_login(user=user)
    response = client.get('/add_training/')
    assert response.status_code == 200
    initial_training_count = Training.objects.count()
    response = client.post('/add_training/', {
        "name": "Nowy trening",
        "description": 5,
        "exercises": exercise.id
    })
    assert response.status_code == 302
    assert Training.objects.count() == initial_training_count + 1


@pytest.mark.django_db
def test_delete_training_view(user, client, training):
    client.force_login(user=user)
    response = client.get(reverse("delete-training", kwargs={"pk": training.id}))
    assert response.status_code == 200
    initial_training_count = Training.objects.count()
    response = client.post(reverse("delete-training", kwargs={"pk": training.id}))
    assert response.status_code == 302
    assert Training.objects.count() == initial_training_count - 1


@pytest.mark.django_db
def test_training_list_view(user, client):
    client.force_login(user=user)
    response = client.get('/training_list/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_training_plan_view_requires_login(user, client):
    response = client.get('/add_training_plan/')
    assert response.status_code == 302
    assert response.url == '/login/?next=/add_training_plan/'
    client.force_login(user=user)
    response = client.get('/add_training_plan/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_training_plan(user, client, training):
    client.force_login(user=user)
    response = client.get('/add_training_plan/')
    assert response.status_code == 200
    initial_training_plan_count = TrainingPlan.objects.count()
    response = client.post('/add_training_plan/', {
        "name": "Nowy plan treningowy",
        "description": 5,
        "trainings": training.id,
        "user_id": user.id
    })
    assert response.status_code == 302
    assert Training.objects.count() == initial_training_plan_count + 1


@pytest.mark.django_db
def test_training_plan_list_view_requires_login(user, client):
    response = client.get('/training_plan_list/')
    assert response.status_code == 302
    assert response.url == '/login/?next=/training_plan_list/'
    client.force_login(user=user)
    response = client.get('/training_plan_list/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_training_plan_list_view(user, client):
    client.force_login(user=user)
    response = client.get('/training_plan_list/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_training_plan_detail_view_requires_login(user, client, training_plan):
    response = client.get(reverse("training-plan-details", kwargs={"pk": training_plan.id}))
    assert response.status_code == 302
    client.force_login(user=user)
    response = client.get(reverse("training-plan-details", kwargs={"pk": training_plan.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_training_plan_detail_view(user, client, training_plan):
    client.force_login(user=user)
    response = client.get(reverse("training-plan-details", kwargs={"pk": training_plan.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_training_plan_view_requires_login(user, client, training_plan):
    response = client.get(reverse("update-training-plan", kwargs={"pk": training_plan.id}))
    assert response.status_code == 302
    client.force_login(user=user)
    response = client.post(reverse("update-training-plan", kwargs={"pk": training_plan.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_training_plan_view(user, client, training, training_plan):
    client.force_login(user=user)
    response = client.get(reverse("update-training-plan", kwargs={"pk": training_plan.id}))
    assert response.status_code == 200
    payload = {
        "name": "Update planu",
        "description": "Nowy opis",
        "trainings": training.id,
        "user_id": user.id
    }
    response = client.post(reverse("update-training-plan", kwargs={"pk": training_plan.id}), data=payload)
    assert response.status_code == 302
    training_plan.refresh_from_db()
    assert training_plan.name == payload['name']
    assert training_plan.description == payload['description']
    assert list(training_plan.trainings.values_list("id", flat=True)) == [payload['trainings']]


@pytest.mark.django_db
def test_update_training_view(user, client, exercise, training):
    client.force_login(user=user)
    response = client.get(reverse("update-training", kwargs={"pk": training.id}))
    assert response.status_code == 200
    payload = {
        "name": "Update treningu",
        "description": "nowy opis",
        "exercises": exercise.id,
    }
    response = client.post(reverse("update-training", kwargs={"pk": training.id}), data=payload)
    assert response.status_code == 302
    print(response.url)
    training.refresh_from_db()
    assert training.name == payload['name']
    assert training.description == payload['description']
    assert list(training.exercises.values_list("id", flat=True)) == [payload['exercises']]


@pytest.mark.django_db
def test_delete_training_plan_view_requires_login(user, client, training_plan):
    response = client.get(reverse("delete-training-plan", kwargs={"pk": training_plan.id}))
    assert response.status_code == 302
    client.force_login(user=user)
    response = client.post(reverse("delete-training-plan", kwargs={"pk": training_plan.id}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_training_plan_view(user, client, training_plan):
    client.force_login(user=user)
    response = client.get(reverse("delete-training-plan", kwargs={"pk": training_plan.id}))
    assert response.status_code == 200
    initial_training_plan_count = TrainingPlan.objects.count()
    response = client.post(reverse("delete-training-plan", kwargs={"pk": training_plan.id}))
    assert response.status_code == 302
    assert TrainingPlan.objects.count() == initial_training_plan_count - 1
