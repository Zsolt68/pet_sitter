from django import forms
from .models import Pet
from django.core.exceptions import ValidationError
from .models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SitterAvailability

# Form for creating and editing Pet instances
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "species", "breed", "age", "notes"]

# Form for creating and editing Booking instances
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "pet",
            "sitter",
            "start_date",
            "end_date",
            "total_price",
            "status",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "total_price": forms.TextInput(
                attrs={"placeholder": "Enter total price",
                }
            )
        }    

# Custom validation for date order and overlapping bookings
    def clean(self):
        cleaned_data = super().clean()
        pet = cleaned_data.get("pet")
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")

        # 1) Validate end_date > start_date
        if start and end and end <= start:
            raise ValidationError("End date must be after start date.")

        # 2) Validate no overlapping bookings for the same pet
        if pet and start and end:
            qs = Booking.objects.filter(pet=pet)

            # Exclude current booking when editing
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            # Overlap condition:
            # (start < existing_end) AND (end > existing_start)
            qs = qs.filter(start_date__lt=end, end_date__gt=start)

            if qs.exists():
                raise ValidationError("This pet already has a booking during that time.")

        return cleaned_data

# Form for creating and updating pet sitter accounts
# Uses Django's built-in User model to manage sitter details
class SitterForm(forms.ModelForm):
    class Meta:
        model = User

        # Fields displayed when creating or updating a sitter profile
        fields = ["username", "first_name", "last_name", "email"]


# Form for creating and editing sitter availability records
class SitterAvailabilityForm(forms.ModelForm):
    class Meta:
        # Use the SitterAvailability model from models.py
        model = SitterAvailability

        # Fields shown in the availability form
        fields = ["sitter", "date", "is_available"]


# Form for creating pet sitter accounts with password creation
# and built-in Django user validation
class SitterForm(UserCreationForm):
    class Meta:
        model = User

        # Fields displayed when creating a new sitter account
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
            ]