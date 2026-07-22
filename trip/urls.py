from django.urls import path

from .views import (
    HomeView,
    NoteCreateView,
    NoteDeleteView,
    NoteDetailView,
    NoteListView,
    NoteUpdateView,
    TripCreateView,
    TripDeleteView,
    TripDetailView,
    TripUpdateView,
    trips_list,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    # Dashboard
    path("dashboard/", trips_list, name="trip-list"),

    # Trips
    path("dashboard/trips/create/", TripCreateView.as_view(), name="trip-create"),
    path("dashboard/trips/<int:pk>/", TripDetailView.as_view(), name="trip-detail"),
    path("dashboard/trips/<int:pk>/update/", TripUpdateView.as_view(), name="trip-update"),
    path("dashboard/trips/<int:pk>/delete/", TripDeleteView.as_view(), name="trip-delete"),

    # Notes
    path("dashboard/notes/", NoteListView.as_view(), name="note-list"),
    path("dashboard/notes/create/", NoteCreateView.as_view(), name="note-create"),
    path("dashboard/notes/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
    path("dashboard/notes/<int:pk>/update/", NoteUpdateView.as_view(), name="note-update"),
    path("dashboard/notes/<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"),
]