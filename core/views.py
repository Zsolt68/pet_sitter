from django.shortcuts import render

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
