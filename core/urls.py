from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import (
    pet_list,
    pet_create,
    pet_update,
    pet_delete,
    booking_list,
    booking_create,
    booking_update,
    booking_delete,
    sitter_list,
    sitter_create,
    sitter_update,
    sitter_delete,
    availability_list,
    availability_create,
    availability_update,
    availability_delete,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("pets/", views.pets, name="pets"),
    path("bookings/", views.bookings, name="bookings"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),

    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),

    # URL routes for pet CRUD: list, add, edit and delete
    path("pets/list/", pet_list, name="pet_list"),
    path("pets/add/", pet_create, name="pet_create"),
    path(
        "pets/<int:pk>/edit/",
        pet_update,
        name="pet_update",
    ),
    path(
        "pets/<int:pk>/delete/",
        pet_delete,
        name="pet_delete",
    ),

    # URL routes for booking CRUD: list, add, edit and delete
    path("bookings/list/", booking_list, name="booking_list"),
    path("bookings/add/", booking_create, name="booking_create"),
    path(
        "bookings/<int:pk>/edit/",
        booking_update,
        name="booking_update",
    ),
    path(
        "bookings/<int:pk>/delete/",
        booking_delete,
        name="booking_delete",
    ),

    # URL routes for sitter CRUD: list, create, update and delete
    path("sitters/", sitter_list, name="sitter_list"),
    path("sitters/add/", sitter_create, name="sitter_create"),
    path(
        "sitters/<int:pk>/edit/",
        sitter_update,
        name="sitter_update",
    ),
    path(
        "sitters/<int:pk>/delete/",
        sitter_delete,
        name="sitter_delete",
    ),

    # URL routes for sitter availability CRUD
    path("availability/", availability_list, name="availability_list"),
    path(
        "availability/create/",
        availability_create,
        name="availability_create",
    ),
    path(
        "availability/update/<int:pk>/",
        availability_update,
        name="availability_update",
    ),
    path(
        "availability/delete/<int:pk>/",
        availability_delete,
        name="availability_delete",
    ),
]
