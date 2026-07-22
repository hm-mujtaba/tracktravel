from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="trips",
    )

    class Meta:
        ordering = ["-start_date", "city"]

    def __str__(self):
        return f"{self.city}, {self.country}"


class Note(models.Model):
    class NoteType(models.TextChoices):
        EVENT = "event", "Event"
        DINING = "dining", "Dining"
        EXPERIENCE = "experience", "Experience"
        GENERAL = "general", "General"

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="notes",
    )

    name = models.CharField(max_length=200)
    description = models.TextField()

    type = models.CharField(
        max_length=20,
        choices=NoteType.choices,
        default=NoteType.GENERAL,
    )

    img = models.ImageField(
        upload_to="notes/",
        blank=True,
        null=True,
    )

    rating = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} ({self.trip.city})"