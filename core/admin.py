from django.contrib import admin
from .models import Pet, Booking, Review, SitterAvailability
# Register your models here.
admin.site.register(Pet)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(SitterAvailability)