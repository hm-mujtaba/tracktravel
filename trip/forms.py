from django import forms

from .models import Note, Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            "city",
            "country",
            "start_date",
            "end_date",
        ]
        widgets = {
            "city": forms.TextInput(
                attrs={
                    "placeholder": "Enter city",
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "placeholder": "Country code (e.g. PK)",
                    "maxlength": 2,
                }
            ),
            "start_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")

        if start and end and end < start:
            raise forms.ValidationError(
                "End date cannot be earlier than the start date."
            )

        return cleaned_data


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            "name",
            "type",
            "rating",
            "description",
            "img",
            "trip",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Write about your experience...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)

        super().__init__(*args, **kwargs)

        if user:
            self.fields["trip"].queryset = Trip.objects.filter(owner=user)