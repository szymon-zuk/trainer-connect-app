from django import forms
from calendar_schedule.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "start_time",
            "end_time",
            "host_email",
            "guest_email",
            "location",
            "event_description",
        ]
        labels = {
            "title": "Nazwa",
            "start_time": "Czas rozpoczęcia",
            "end_time": "Czas zakończenia",
            "host_email": "E-mail trenera",
            "guest_email": "E-mail podopiecznego",
            "location": "Lokalizacja",
            "event_description": "Opis spotkania",
        }
