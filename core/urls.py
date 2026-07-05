from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import (
    pet_list, pet_create, pet_update, pet_delete,
    booking_list, booking_create, booking_update, booking_delete,
    sitter_list, sitter_create, sitter_update, sitter_delete,
    availability_list, availability_create, availability_update, availability_delete,
)

urlpatterns = [
    path('', views.home, name='home'),
    path("pets/", views.pets, name="pets"),
    path("bookings/", views.bookings, name="bookings"),
    path("login/", views.login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    
    # URL routes for pet CRUD: list, add, edit and delete
    path("pets/list/", views.pet_list, name="pet_list"),
    path("pets/add/", views.pet_create, name="pet_create"),
    path("pets/<int:pk>/edit/", views.pet_update, name="pet_update"),
    path("pets/<int:pk>/delete/", views.pet_delete, name="pet_delete"),

    # URL routes for booking CRUD: list, add, edit and delete
    path("bookings/list/", views.booking_list, name="booking_list"),
    path("bookings/add/", views.booking_create, name="booking_create"),
    path("bookings/<int:pk>/edit/", views.booking_update, name="booking_update"),
    path("bookings/<int:pk>/delete/", views.booking_delete, name="booking_delete"),

    # URL routes for sitter CRUD: list, create, update and delete
    path("sitters/", views.sitter_list, name="sitter_list"),
    path("sitters/add/", views.sitter_create, name="sitter_create"),
    path("sitters/<int:pk>/edit", views.sitter_update, name="sitter_update"),
    path("sitters/<int:pk>/delete", views.sitter_delete, name="sitter_delete"),

    # URL routes for sitter availability CRUD: list, create, update and delete
    path("availability/", availability_list, name="availability_list"),
    path("availability/create/", availability_create, name="availability_create"),
    path("availability/update/<int:pk>/", availability_update, name="availability_update"),
    path("availability/delete/<int:pk>/", availability_delete, name="availability_delete"),

]
