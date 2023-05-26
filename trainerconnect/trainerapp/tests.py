from django.test import Client
from . models import Exercise

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
    ctx = {
        "name": "Update ćwiczenia",
        "sets": 6,
        "reps": 6,
        "load": 120,
        "comment": "Nowszy komentarz"
    }
    response = client.post("/update_exercise/", ctx)
    assert response.status_code == 302
    assert exercise.name == "Update ćwiczenia"
    assert exercise.sets == 6
    assert exercise.reps == 6
    assert exercise.load == 120
    assert exercise.comment == "Nowszy komentarz"
    
