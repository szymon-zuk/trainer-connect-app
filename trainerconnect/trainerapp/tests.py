from django.test import Client
from . models import Exercise, Training, TrainingPlan

def test_main():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_exercise_view_requires_login(user, client):
    response = client.get('/add_exercise/')
    assert response.status_code == 302
    assert response.url == '/add_exercise/'
    client.force_login(user=user)
    response = client.get('/add_exercise/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_exercise_list_view_requires_login(user, client):
    response = client.get('/exercise_list/')
    assert response.status_code == 302
    assert response.url == '/exercise_list/'
    client.force_login(user=user)
    response = client.get('/exercise_list/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_exercise_list_view_requires_login(user, client):
    response = client.get('/update_exercise/')
    assert response.status_code == 302
    assert response.url == '/update_exercise/'
    client.force_login(user=user)
    response = client.get('/update_exercise/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_exercise_view(client):
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
def test_delete_exercise_view(client):
    response = client.get('/delete_exercise/')
    assert response.status_code == 200
    initial_exercise_count = Exercise.objects.count()
    response = client.post('/delete_exercise/')
    assert response.status_code == 302
    assert Exercise.objects.count() == initial_exercise_count - 1

@pytest.mark.django_db
def test_exercise_list_view(client, exercise):
    response = client.get('/exercise_list/')
    exercises = Exercise.objects.all()
    assert response.status_code == 200
    assert len(response.context['object_list']) == 1
    assert response.context['object_list'][0] == exercise

@pytest.mark.django_db
def test_update_exercise_view(client, exercise):
    response = client.get('/update_exercise/')
    assert response.status_code == 200
    payload = {
        "name": "Update ćwiczenia",
        "sets": 6,
        "reps": 6,
        "load": 120,
        "comment": "Nowszy komentarz"
    }
    response = client.post("/update_exercise/", payload)
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
    assert response.url == '/add_training/'
    client.force_login(user=user)
    response = client.get('/add_training/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_training_list_view_requires_login(user, client):
    response = client.get('/training_list/')
    assert response.status_code == 302
    assert response.url == '/training_list/'
    client.force_login(user=user)
    response = client.get('/training_list/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_training_list_view_requires_login(user, client):
    response = client.get('/update_training/')
    assert response.status_code == 302
    assert response.url == '/update_training/'
    client.force_login(user=user)
    response = client.get('/update_training/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_training_view(client):
    response = client.get('/add_training/')
    assert response.status_code == 200
    initial_training_count = Training.objects.count()
    new_exercise = Exercise.objects.last()
    response = client.post('/add_training/', {
        "name": "Nowy trening",
        "description": 5,
        "exercises": new_exercise
    })
    assert response.status_code == 302
    assert Training.objects.count() == initial_training_count + 1

@pytest.mark.django_db
def test_delete_training_view(client):
    response = client.get('/delete_training/')
    assert response.status_code == 200
    initial_training_count = Training.objects.count()
    response = client.post('/delete_training/')
    assert response.status_code == 302
    assert Training.objects.count() == initial_training_count - 1

@pytest.mark.django_db
def test_training_list_view(client, training):
    response = client.get('/training_list/')
    trainings = Training.objects.all()
    assert response.status_code == 200
    assert len(response.context['object_list']) == 1
    assert response.context['object_list'][0] == training

# dopisać test_training_update_view()