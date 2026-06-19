from django.contrib import admin
from .models import Pet, Booking, Review, SitterAvailability

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "owner")
    search_fields = ("name", "species", "owner__username")
    list_filter = ("species",)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("pet", "owner", "sitter", "start_date", "end_date", "status")
    search_fields = ("pet__name", "owner__username", "sitter__username")
    list_filter = ("status", "start_date", "end_date")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("rating", "written_by", "written_for", "created_at")
    search_fields = ("written_by__username", "written_for__username")
    list_filter = ("rating", "created_at")


@admin.register(SitterAvailability)
class SitterAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("sitter", "date", "is_available")
    search_fields = ("sitter__username",)
    list_filter = ("is_available", "date")