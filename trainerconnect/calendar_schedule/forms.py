from django import forms
from calendar_schedule.models import Event


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            "title",
            "start",
            "end",
            "location",
            "event_description",
        ]
        labels = {
            "title": "Nazwa",
            "start": "Czas rozpoczęcia",
            "end": "Czas zakończenia",
            "location": "Lokalizacja",
            "event_description": "Opis spotkania",
        }
        widgets = {
            "start": DateTimeInput(),
            'end': DateTimeInput()
        }
