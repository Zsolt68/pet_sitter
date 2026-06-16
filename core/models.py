from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pet(models.Model):
    """Represents a pet owned by a user."""

    # Link each pet to a user. If the user is deleted, delete their pets.
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pets"
    )

