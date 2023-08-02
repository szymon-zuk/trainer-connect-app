from calendar_schedule.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import EventForm
from .API import create_event, edit_event


class CreateEventView(SuccessMessageMixin, LoginRequiredMixin, View):
    """This view adds new event to db and to google calendar"""

    success_message = "Event created!"

    def get(self, request):
        form = EventForm()
        return render(request, "create_event_view.html", {"form": form})

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            location = form.cleaned_data["location"]
            event_description = form.cleaned_data["event_description"]
            create_event(
                title,
                start,
                end,
                location,
                event_description,
            )
            form.save()
            return redirect("event-list")
        return render(request, "event_list.html", {"form": form})


class EventListView(LoginRequiredMixin, View):
    def get(self, request):
        event_list = Event.objects.all()
        return render(request, "event_list.html", {"object": event_list})


class UpdateEventView(SuccessMessageMixin, LoginRequiredMixin, View):
    """View that updates an event in db and in google calendar"""

    def get(self, request):
        form = EventForm()
        return render(request, "update_event_view.html", {"form": form})

    def post(self, request):
        form = EventForm()
        if form.is_valid():
            title = form.cleaned_data["title"]
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            location = form.cleaned_data["location"]
            event_description = form.cleaned_data["event_description"]
            edit_event(
                title,
                start,
                end,
                location,
                event_description,
            )
            form.save()
            return redirect("event-list")
        return render(request, "event_list.html", {"form": form})
