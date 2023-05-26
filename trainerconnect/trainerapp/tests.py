from django.test import Client


def test_main():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200

def test_training_list_login_required():
    client = Client()
    response = client.get('/training_list/')
    assert response.status_code == 302
    assert response.url == '/login/'