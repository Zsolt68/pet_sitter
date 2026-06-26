from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import PetForm
from .models import Booking
from .forms import BookingForm

# Core placeholder views for each page in the site

def home(request):
    return render(request, "core/home.html")

def pets(request):
    return render(request, "core/pets.html")

def bookings(request):
    return render(request, "core/bookings.html")

def sitters(request):
    return render(request, "core/sitters.html")

def login(request):
    return render(request, "core/login.html")

def register(request):
    return render(request, "core/register.html")

# Display a list of pets that belong to the currently logged‑in user.
# Requires authentication; unauthenticated users are redirected to login.
@login_required
def pet_list(request):
    pets = Pet.objects.filter(owner=request.user)
    return render(request, "core/pets/list.html", {"pets": pets})

# Handle creating a new pet for the logged‑in user
@login_required
def pet_create(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            messages.success(request, "Pet added successfully.")
            return redirect("pet_list")
        else:
            messages.error(request, "Please correct the errors below.")        
    else:
        form = PetForm()
    return render(request, "core/pets/form.html", {"form": form, "title": "Add Pet"})

# Handle editing an existing pet owned by the logged‑in user
@login_required
def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk, owner=request.user)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, "Pet updated successfully.")
            return redirect("pet_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PetForm(instance=pet)
    return render(request, "core/pets/form.html", {"form": form, "title": "Edit Pet"})

# Handle deleting an existing pet owned by the logged‑in user
@login_required
def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk, owner=request.user)
    if request.method == "POST":
        pet.delete()
        messages.success(request, "Pet deleted successfully.")
        return redirect("pet_list")
    return render(request, "core/pets/delete.html", {"pet": pet})

# CRUD views for managing Booking records; includes list, create, and update
@login_required
def booking_list(request):
    bookings = Booking.objects.filter(owner=request.user)
    return render(request, "core/bookings/list.html", {"bookings": bookings})

@login_required
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.owner = request.user
            booking.save()
            messages.success(request, "Booking created successfully.")
            return redirect("booking_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm()
    return render(request, "core/bookings/form.html", {"form": form, "title": "Add Booking"})

@login_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk, owner=request.user)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully.")
            return redirect("booking_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm(instance=booking)
    return render(request, "core/bookings/form.html", {"form": form, "title": "Edit Booking"})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, owner=request.user)
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect("booking_list")
    return render(request, "core/bookings/delete.html", {"booking": booking})

