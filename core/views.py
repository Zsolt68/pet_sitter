from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Pet, Booking

from .forms import SitterAvailability, SitterForm, SitterAvailabilityForm
from .forms import PetForm, BookingForm, RegisterForm

# Core placeholder views for each page in the site
@login_required
def home(request):
    return render(request, "home.html")
@login_required
def pets(request):
    return render(request, "pets.html")
@login_required
def bookings(request):
    return render(request, "bookings.html")
@login_required
def sitters(request):
    return render(request, "sitters.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # Handle ?next=/availability/ redirect
            next_url = request.POST.get("next") or request.GET.get("next")
            if next_url:
                return redirect(next_url)

            return redirect("home")

        return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")

# Handle user registration with validation, messages and redirect to login
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

# Display a list of pets that belong to the currently logged‑in user.
# Requires authentication; unauthenticated users are redirected to login.
@login_required
def pet_list(request):
    pets = Pet.objects.filter(owner=request.user)
    return render(request, "pets/list.html", {"pets": pets})

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
    return render(request, "pets/form.html", {"form": form, "title": "Add Pet"})

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
    return render(request, "pets/form.html", {"form": form, "title": "Edit Pet"})

# Handle deleting an existing pet owned by the logged‑in user
@login_required
def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk, owner=request.user)
    if request.method == "POST":
        pet.delete()
        messages.success(request, "Pet deleted successfully.")
        return redirect("pet_list")
    return render(request, "pets/delete.html", {"pet": pet})

# CRUD views for managing Booking records; includes list, create, and update
@login_required
def booking_list(request):
    bookings = Booking.objects.filter(owner=request.user)
    return render(request, "bookings/list.html", {"bookings": bookings})

@login_required
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.owner = request.user
            booking.save()
            # Display success message after creating a booking
            messages.success(request, "Booking created successfully.")
            return redirect("booking_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm()
    return render(request, "bookings/form.html", {"form": form, "title": "Add Booking"})

@login_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk, owner=request.user)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            # Display success message after updating a booking
            messages.success(request, "Booking updated successfully.")
            return redirect("booking_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm(instance=booking)
    return render(request, "bookings/form.html", {"form": form, "title": "Edit Booking"})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, owner=request.user)
    if request.method == "POST":
        booking.delete()
        # Display success message after deleting a booking
        messages.success(request, "Booking deleted successfully.")
        return redirect("booking_list")
    return render(request, "bookings/delete.html", {"booking": booking})

# Display all sitters in a list
@login_required
def sitter_list(request):
    sitters = User.objects.all()
    return render(request, "sitters/list.html", {"sitters": sitters})    

# Create a new sitter and display a success message after saving
@login_required
def sitter_create(request):
    if request.method == "POST":
        form = SitterForm(request.POST)
        if form.is_valid():
            form.save()
            # Success message for sitter creation
            messages.success(request, "Sitter added successfully.")
            return redirect("sitter_list")
    else:
        form = SitterForm()

    return render(request, "sitters/form.html", {"form": form})

# Update an existing sitter and show a success message when changes are saved
@login_required
def sitter_update(request, pk):
    sitter = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        form = SitterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            # Success message for sitter update
            messages.success(request, "Sitter updated successfully.")
            return redirect("sitter_list")
    else:
        form = SitterForm(instance=sitter)

    return render(request, "sitters/form.html", {"form": form})

# Delete a sitter after confirmation and show a success message
@login_required    
def sitter_delete(request, pk):
    sitter = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        sitter.delete()
        # Success message for sitter deletion
        messages.success(request, "Sitter deleted successfully.")
        return redirect("sitter_list")

    return render(request, "sitters/delete.html", {"sitter": sitter})

# List all sitter availability entries
@login_required
def availability_list(request):
    # Fetch all availability records from the database
    availability_list = SitterAvailability.objects.all()

    # Render the list template with the availability data
    return render(
        request,
        "availability/list.html",
        {"availability_list": availability_list}
    )

# Create a new availability entry
@login_required
def availability_create(request):
    if request.method == "POST":
        # Bind POST data to the form
        form = SitterAvailabilityForm(request.POST)

        # Validate and save the new availability entry
        if form.is_valid():
            form.save()
            messages.success(request, "Availability added successfully.")
            return redirect("availability_list")
    else:
        # Display an empty form for GET requests
        form = SitterAvailabilityForm()

    # Render the form template
    return render(request, "availability/form.html", {"form": form})


# Update an existing availability entry
@login_required
def availability_update(request, pk):
    # Fetch the availability entry or return 404
    availability = get_object_or_404(SitterAvailability, pk=pk)

    if request.method == "POST":
        # Bind POST data to the form with the existing instance
        form = SitterAvailabilityForm(request.POST, instance=availability)

        # Validate and save the updated entry
        if form.is_valid():
            form.save()
            messages.success(request, "Availability updated successfully.")
            return redirect("availability_list")
    else:
        # Display the form with existing data for GET requests
        form = SitterAvailabilityForm(instance=availability)

    # Render the form template
    return render(request, "availability/form.html", {"form": form})


# Delete an availability entry after confirmation
@login_required
def availability_delete(request, pk):
    # Fetch the availability entry or return 404
    availability = get_object_or_404(SitterAvailability, pk=pk)

    if request.method == "POST":
        # Delete the entry and show a success message
        availability.delete()
        messages.success(request, "Availability deleted successfully.")
        return redirect("availability_list")

    # Render the delete confirmation template
    return render(
        request,
        "availability/delete.html",
        {"availability": availability}
    )



