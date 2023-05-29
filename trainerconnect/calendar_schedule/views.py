from calendar_schedule.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import  View
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from apiclient.discovery import build
import pickle
from calendar_schedule.API import GoogleCalendar


class CreateEventView(SuccessMessageMixin, LoginRequiredMixin, View):
    """This view adds new event to db and to google calendar"""
    def get(self, request):
        form = EventForm()
        return render(request, 'create_event_view.html', {'form': form})
        
    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            start_time = form.cleaned_data['start']
            end_time = form.cleaned_data['end']
            host_email = form.cleaned_data['host_email']
            guest_email = form.cleaned_data['guest_email']
            location = form.cleaned_data['location']
            event_description = form.cleaned_data['event_description']
            GoogleCalendar.send_to_API(title, start_time, end_time, host_email, guest_email, location, event_description)

            """assign event_id from google calendar to event_id of the form"""
            replace = form.save(commit=False)
            replace.event_id = GoogleCalendar.get_event_id()
            replace.save()
            form.save()
            return redirect('event:home')
        return render(request, "create_event.html", {'form': form})
    

class EventListView(LoginRequiredMixin, View):
    def get(self, request):

        event_list = Event.objects.all()
        return render(request, 'my_events.html', {'object': event_list})