from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.shortcuts import render
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta


def create_event(request):
    # Ścieżka do pliku JSON z danymi uwierzytelniającymi
    credentials = service_account.Credentials.from_service_account_file(
        '/home/szymon/Desktop/trainer-connect-app/trainerconnect/calendar_schedule/credentials.json',
        scopes=['https://www.googleapis.com/auth/calendar']
    )

    # Inicjalizacja klienta API
    service = build('calendar', 'v3', credentials=credentials)

    # Tworzenie nowego wydarzenia
    event = {
        'summary': 'Przykładowe wydarzenie',
        'start': {
            'dateTime': '2023-05-24T10:00:00',
            'timeZone': 'Europe/Warsaw',
        },
        'end': {
            'dateTime': '2023-05-24T12:00:00',
            'timeZone': 'Europe/Warsaw',
        },
    }

    # Wysłanie żądania API do utworzenia wydarzenia


def get_events(request):
    # Ścieżka do pliku JSON z danymi uwierzytelniającymi
    credentials = service_account.Credentials.from_service_account_file(
        '/home/szymon/Desktop/trainer-connect-app/trainerconnect/calendar_schedule/credentials.json',
        scopes=['https://www.googleapis.com/auth/calendar']
    )

    # Inicjalizacja klienta API
    service = build('calendar', 'v3', credentials=credentials)

    # Obliczanie daty początkowej i końcowej tygodnia
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    # Pobieranie wydarzeń dla określonego tygodnia
    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_of_week.isoformat() + 'Z',
        timeMax=end_of_week.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    return render(request, 'events.html', {'events': events})
