from django.contrib import admin

from .models import Note, Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "country",
        "owner",
        "start_date",
        "end_date",
    )
    list_filter = (
        "country",
        "start_date",
    )
    search_fields = (
        "city",
        "owner__username",
    )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "trip",
        "type",
        "rating",
    )
    list_filter = (
        "type",
        "rating",
    )
    search_fields = (
        "name",
        "trip__city",
        "trip__owner__username",
    )