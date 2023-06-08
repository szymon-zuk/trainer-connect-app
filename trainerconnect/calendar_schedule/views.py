from calendar_schedule.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm
from apiclient.discovery import build
from .API import create_event


# def demo(request):
#     results = create_event()
#     context = {"results": results}
#     return render(request, "event_list.html", context)


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
