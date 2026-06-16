from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pet(models.Model):
    """Represents a pet owned by a user."""

    # Link each pet to a user. If the user is deleted, delete their pets.
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pets"
    )

# Basic pet details
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField()

    # Optional notes about the pet
    notes = models.TextField(blank=True)

    def __str__(self):
        # Display pet name and owner for clarity in admin
        return f"{self.name} ({self.owner.username})"

class Booking(models.Model):
    """Represents a booking between an owner and a sitter."""

    # The pet being booked
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="bookings"
    )

    # The user who owns the pet
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner_bookings"
    )

    # The user who will sit the pet
    sitter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sitter_bookings"
    )

    # Booking date range
    start_date = models.DateField()
    end_date = models.DateField()

    # Track booking status
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
            ("completed", "Completed"),
        ],
        default="pending",
    )

    # Total price for the booking
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    # Auto-set when the booking is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Show pet name and status for admin readability
        return f"Booking for {self.pet.name} ({self.status})"