from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import PetForm

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
            return redirect("pet_list")
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
            return redirect("pet_list")
    else:
        form = PetForm(instance=pet)
    return render(request, "core/pets/form.html", {"form": form, "title": "Edit Pet"})
