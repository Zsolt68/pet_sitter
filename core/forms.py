# Form for creating and editing Pet instances
from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "species", "breed", "age", "notes"]

# Form for creating and editing Booking instances
from .models import Booking

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