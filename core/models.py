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