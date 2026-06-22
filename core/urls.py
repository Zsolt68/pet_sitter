from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("pets/", views.pets, name="pets"),
    path("bookings/", views.bookings, name="bookings"),
    path("sitters/", views.sitters, name="sitters"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    
    # List pets belonging to the logged‑in user
    path("pets/list/", views.pet_list, name="pet_list"),

]
