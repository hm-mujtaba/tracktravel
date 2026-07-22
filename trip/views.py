from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import NoteForm, TripForm
from .models import Note, Trip


class UserTripMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.get_object().owner == self.request.user


class UserNoteMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.get_object().trip.owner == self.request.user


class HomeView(TemplateView):
    template_name = "trip/index.html"


@login_required
def trips_list(request):
    trips = (
        Trip.objects.filter(owner=request.user)
        .prefetch_related("notes")
    )
    return render(request, "trip/trip_list.html", {"trips": trips})


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    form_class = TripForm
    success_url = reverse_lazy("trip-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TripDetailView(UserTripMixin, DetailView):
    model = Trip
    queryset = Trip.objects.prefetch_related("notes")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = self.object.notes.all()
        return context


class TripUpdateView(UserTripMixin, UpdateView):
    model = Trip
    form_class = TripForm
    success_url = reverse_lazy("trip-list")


class TripDeleteView(UserTripMixin, DeleteView):
    model = Trip
    success_url = reverse_lazy("trip-list")


class NoteListView(LoginRequiredMixin, ListView):
    model = Note

    def get_queryset(self):
        return (
            Note.objects.filter(trip__owner=self.request.user)
            .select_related("trip")
        )


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("note-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class NoteDetailView(UserNoteMixin, DetailView):
    model = Note
    queryset = Note.objects.select_related("trip")


class NoteUpdateView(UserNoteMixin, UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("note-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class NoteDeleteView(UserNoteMixin, DeleteView):
    model = Note
    success_url = reverse_lazy("note-list")