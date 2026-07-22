from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Trip, Note
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = "trip/index.html"


@login_required
def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        "trips": trips,
    }
    return render(request, "trip/trip_list.html", context)


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ["city", "country", "start_date", "end_date"]
    success_url = reverse_lazy("trip-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip

    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context["object"]
        context["notes"] = trip.notes.all()
        return context


class TripUpdateView(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = ["city", "country", "start_date", "end_date"]
    success_url = reverse_lazy("trip-list")

    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)


class TripDeleteView(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = reverse_lazy("trip-list")

    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)


class NoteListView(LoginRequiredMixin, ListView):
    model = Note

    def get_queryset(self):
        return Note.objects.filter(trip__owner=self.request.user)


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note

    def get_queryset(self):
        return Note.objects.filter(trip__owner=self.request.user)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ["name", "type", "rating", "description", "img", "trip"]
    success_url = reverse_lazy("note-list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["trip"].queryset = Trip.objects.filter(owner=self.request.user)
        return form


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = "__all__"
    success_url = reverse_lazy("note-list")

    def get_queryset(self):
        return Note.objects.filter(trip__owner=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["trip"].queryset = Trip.objects.filter(owner=self.request.user)
        return form


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy("note-list")

    def get_queryset(self):
        return Note.objects.filter(trip__owner=self.request.user)