from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("pets/", views.pets, name="pets"),
    path("bookings/", views.bookings, name="bookings"),
    path("sitters/", views.sitters, name="sitters"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    
    # List pets belonging to the logged‑in user or Pet CRUD
    path("pets/list/", views.pet_list, name="pet_list"),
    path("pets/add/", views.pet_create, name="pet_create"),
    path("pets/<int:pk>/edit/", views.pet_update, name="pet_update"),
    path("pets/<int:pk>/delete/", views.pet_delete, name="pet_delete"),

    # List bookings belonging to the logged‑in user or Booking CRUD
    path("bookings/list/", views.booking_list, name="booking_list"),
    path("bookings/add/", views.booking_create, name="booking_create"),
    path("bookings/<int:pk>/edit/", views.booking_update, name="booking_update"),
    path("bookings/<int:pk>/delete/", views.booking_delete, name="booking_delete"),

]
