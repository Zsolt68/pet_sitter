# pet_sitter

 # Title
# Badges

## Table of Contents

## Project Overview

## UX
The UX design follows the five‑plane model: Strategy, Scope, Structure, Skeleton, and Surface.  
The goal is to provide a clean, intuitive interface for managing pets and bookings with minimal friction.

---

### Strategy

The primary goals of the application are:

- Allow pet owners to manage their pets
- Allow users to create sitter bookings
- Prevent invalid or overlapping bookings
- Provide a simple, mobile‑friendly interface
- Ensure users can only access their own data

Target users:

- Pet owners
- Pet sitters (future enhancement)
- Admin users (future enhancement)

---

### 📦 Scope

**Functional Requirements**
- User authentication
- CRUD for pets
- CRUD for bookings
- Booking validation (date order + overlap prevention)
- Responsive UI

**Non‑Functional Requirements**
- Fast and intuitive navigation
- Clear error/success feedback
- Secure access control

---

### Structure

The application follows a clear hierarchical structure:

- Navigation bar → Pets / Bookings / Login / Logout
- Pets section → list, add, edit, delete
- Bookings section → list, add, edit, delete
- Validation errors displayed inline
- Success messages displayed via Django messages

---

### 🦴Skeleton
ireframes were created to outline the layout of each page.

#### **Wireframes**

```
+--------------------------------------------------+
| Navigation Bar                                   |
+--------------------------------------------------+
| Page Title                                       |
|                                                  |
| [Action Button]                                  |
|                                                  |
| Table / Form / Confirmation Box                  |
|                                                  |
+--------------------------------------------------+
| Footer                                           |
+--------------------------------------------------+
```

Mobile layout collapses navigation and stacks content vertically.

---

### 🎨 Surface

The visual design uses:

- Bootstrap 5 for layout and components
- Clean spacing and typography
- Consistent button styles
- Clear form labels and validation messages
- Mobile‑first responsive design

## Features

## User Stories

## Project Structure

## Models

## Booking Validation

## Flowchart

## Testing
### Manual Testing
### Validation Testing
### Browser Testing
### Code Validation

## Lighthouse Report

## Deployment

## Future Enhancements

## Credits & Acknowledgements


# Pet Sitter Booking System

A full‑stack Django application that allows users to manage their pets and create sitter bookings with built‑in validation, authentication, and a clean Bootstrap UI.

![GitHub last commit](badge)
![Heroku deployment](badge)
![Python version](badge)

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [User Stories](#user-stories)
- [Project Structure](#project-structure)
- [Models](#models)
- [Booking Validation](#booking-validation)
- [Flowchart](#flowchart)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Credits & Acknowledgements](#credits--acknowledgements)

---

## Project Overview

This project provides a simple and intuitive platform for pet owners to manage their pets and create sitter bookings. It includes full CRUD functionality for Pets and Bookings, user authentication, and custom validation to prevent overlapping bookings.

---

## Project Structure

The project follows a clean and modular Django structure, separating concerns across apps, templates, static files, and configuration.

```
project-root/
│
├── manage.py
├── requirements.txt
├── Procfile
│
├── codestar/                     # Main Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/                         # Main application (Pets + Bookings)
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   └── templates/
│       └── core/
│           ├── base.html
│           │
│           ├── pets/
│           │   ├── list.html
│           │   ├── form.html
│           │   └── delete.html
│           │
│           └── bookings/
│               ├── list.html
│               ├── form.html
│               └── delete.html
│
└── static/                       # CSS, JS, images
    └── css/
        └── style.css
```

## User Stories

### As a **pet owner**, I want to:
- Create an account so I can manage my pets and bookings.
- Add my pets to the system so I can book sitters for them.
- Edit or delete pet information to keep details up to date.
- View all my pets in one place for easy management.

### As a **pet owner**, I want to:
- Create bookings for my pets so they can be cared for.
- Edit bookings if plans change.
- Delete bookings I no longer need.
- See all my bookings in a clear list.

### As a **system**, I must:
- Prevent overlapping bookings for the same pet.
- Ensure booking dates are valid.
- Restrict access so users can only manage their own data.
- Provide clear feedback when actions succeed or fail.


## Features

### 🐾 Pet Management (CRUD)
- Add new pets with details (name, species, breed, age)
- Edit existing pet information
- Delete pets with confirmation
- View all pets belonging to the logged‑in user

### 📅 Booking Management (CRUD)
- Create bookings for a selected pet and sitter
- Edit booking details
- Delete bookings with confirmation
- View all bookings belonging to the logged‑in user

### 🔒 Authentication
- User registration
- Login/logout
- Access control (only owners can manage their pets and bookings)

### ✔ Booking Validation
- Prevent overlapping bookings for the same pet
- Ensure end date is after start date
- Clean error messages displayed in the form

### 🎨 Responsive UI
- Clean Bootstrap layout
- Navigation bar with dynamic links
- Mobile‑friendly design

### 📢 User Feedback
- Success and error messages using Django’s messages framework

### 🚀 Deployment Ready
- Works with cloud deployment platforms
- Static files collected and served correctly


## Data Models

The project uses four core models:

### Pet
Stores information about a pet owned by a user.

### Booking
Represents a booking between a pet owner and a sitter.

### Review
A review left by a user after a completed booking.

### SitterAvailability
Stores the available dates for each sitter.

These models form the foundation of the Pet Sitter platform and
enable CRUD operations, user interactions, and booking workflows.


## Application Architecture — Pets & Bookings

This project uses a clean, modular Django architecture with two main CRUD systems: **Pets** and **Bookings**.

```
+---------------------------------------------------------------+
|                           MODELS                              |
+---------------------------------------------------------------+
| Pet                                                           |
|  - name                                                       |
|  - species                                                    |
|  - breed                                                      |
|  - age                                                        |
|  - owner (FK → User)                                         |
|                                                               |
| Booking                                                       |
|  - pet (FK → Pet)                                            |
|  - sitter (FK → User)                                        |
|  - start_date                                                 |
|  - end_date                                                   |
|  - total_price                                                |
|  - status                                                     |
|  - owner (FK → User)                                         |
+---------------------------------------------------------------+

+---------------------------------------------------------------+
|                           FORMS                               |
+---------------------------------------------------------------+
| PetForm                                                       |
| BookingForm                                                   |
|  - Includes custom validation                                 |
|    • end_date > start_date                                    |
|    • no overlapping bookings                                  |
+---------------------------------------------------------------+

+---------------------------------------------------------------+
|                           VIEWS                               |
+---------------------------------------------------------------+
| Pets:                                                         |
|  - pet_list                                                   |
|  - pet_create                                                 |
|  - pet_update                                                 |
|  - pet_delete                                                 |
|                                                               |
| Bookings:                                                     |
|  - booking_list                                               |
|  - booking_create                                             |
|  - booking_update                                             |
|  - booking_delete                                             |
+---------------------------------------------------------------+

+---------------------------------------------------------------+
|                         TEMPLATES                             |
+---------------------------------------------------------------+
| core/pets/                                                    |
|   - list.html                                                 |
|   - form.html                                                 |
|   - delete.html                                               |
|                                                               |
| core/bookings/                                                |
|   - list.html                                                 |
|   - form.html                                                 |
|   - delete.html                                               |
+---------------------------------------------------------------+

+---------------------------------------------------------------+
|                           URLS                                |
+---------------------------------------------------------------+
| /pets/list/                                                   |
| /pets/add/                                                    |
| /pets/<id>/edit/                                              |
| /pets/<id>/delete/                                            |
|                                                               |
| /bookings/list/                                               |
| /bookings/add/                                                |
| /bookings/<id>/edit/                                          |
| /bookings/<id>/delete/                                        |
+---------------------------------------------------------------+
```


## Booking Process Flowchart

Below is a simplified flowchart showing how the booking process works from the user's perspective.

```
                ┌────────────────────┐
                │  User selects pet  │
                └─────────┬──────────┘
                          ▼
                ┌────────────────────┐
                │ User selects dates │
                └─────────┬──────────┘
                          ▼
                ┌────────────────────┐
                │  Submit booking    │
                └─────────┬──────────┘
                          ▼
                ┌────────────────────────────────────────┐
                │ Run validation:                        │
                │  - End date > start date               │
                │  - No overlapping bookings for pet     │
                └─────────┬──────────────────────────────┘
                          ▼
        ┌──────────────────────────┬──────────────────────────┐
        ▼                          ▼                          ▼
┌───────────────┐        ┌────────────────┐        ┌──────────────────────┐
│ Validation OK  │        │ Date invalid   │        │ Overlap detected     │
└───────┬────────┘        └───────┬────────┘        └──────────┬──────────┘
        ▼                          ▼                             ▼
┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
│ Save booking to DB   │   │ Show error message   │   │ Show error message   │
└─────────┬────────────┘   └─────────┬────────────┘   └─────────┬────────────┘
          ▼                            ▼                          ▼
┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
│ Redirect to list     │   │ User corrects input  │   │ User adjusts dates   │
└──────────────────────┘   └──────────────────────┘   └──────────────────────┘
```

## Booking Validation

To ensure data integrity and prevent scheduling conflicts, the Booking system includes custom validation logic implemented in the `BookingForm.clean()` method.

### ✔ 1. End Date Must Be After Start Date
A booking is only valid if the end date occurs after the start date.

```
if end <= start:
    raise ValidationError("End date must be after start date.")
```

This prevents invalid entries such as:
- End date earlier than start date  
- End date equal to start date  

---

### ✔ 2. Prevent Overlapping Bookings for the Same Pet
A pet cannot have two bookings that overlap in time.  
The system checks all existing bookings for the same pet and applies the universal overlap rule:

```
(start < existing_end) AND (end > existing_start)
```

If any overlapping booking exists, validation fails:

```
raise ValidationError("This pet already has a booking during that time.")
```

This ensures that each pet can only be booked for one sitter at a time.

---

### 📘 Visual Timeline Diagram

```
1) OVERLAPPING BOOKINGS (❌ Not Allowed)

   Existing booking:   |────── 10 Jun → 15 Jun ──────|
   New booking:              |──── 14 Jun → 20 Jun ────|

2) NON‑OVERLAPPING BOOKINGS — AFTER (✔ Allowed)

   Existing booking:   |────── 10 Jun → 15 Jun ──────|
   New booking:                                   |── 16 Jun → 20 Jun ──|

3) NON‑OVERLAPPING BOOKINGS — BEFORE (✔ Allowed)

   New booking:     |── 01 Jun → 05 Jun ──|
   Existing booking:                 |────── 10 Jun → 15 Jun ──────|
```


+---------------------------------------------------------------+
|                 BOOKING DATE RANGE VALIDATION                 |
+---------------------------------------------------------------+

1) OVERLAPPING BOOKINGS (❌ Not Allowed)

   Existing booking:   |────── 10 Jun → 15 Jun ──────|
   New booking:              |──── 14 Jun → 20 Jun ────|

   Overlap occurs because:
     - New start (14 Jun) < existing end (15 Jun)
     - New end (20 Jun) > existing start (10 Jun)


2) NON‑OVERLAPPING BOOKINGS — AFTER (✔ Allowed)

   Existing booking:   |────── 10 Jun → 15 Jun ──────|
   New booking:                                   |── 16 Jun → 20 Jun ──|

   No overlap:
     - New start (16 Jun) > existing end (15 Jun)


3) NON‑OVERLAPPING BOOKINGS — BEFORE (✔ Allowed)

   New booking:     |── 01 Jun → 05 Jun ──|
   Existing booking:                 |────── 10 Jun → 15 Jun ──────|

   No overlap:
     - New end (05 Jun) < existing start (10 Jun)


4) OVERLAP RULE USED IN VALIDATION

   Two bookings overlap if BOTH are true:
     (new_start < existing_end)
       AND
     (new_end > existing_start)

   If both conditions are true → ❌ Overlap detected
   If either condition is false → ✔ Safe booking

## Testing

### ✔ Manual Testing

#### **Pets**
| Feature | Expected Result | Test Result |
|--------|-----------------|-------------|
| Add Pet | Pet is created and visible in list | ✔ Passed |
| Edit Pet | Changes saved and displayed | ✔ Passed |
| Delete Pet | Pet removed after confirmation | ✔ Passed |
| Access Control | Users cannot access others’ pets | ✔ Passed |

#### **Bookings**
| Feature | Expected Result | Test Result |
|--------|-----------------|-------------|
| Add Booking | Booking created and visible | ✔ Passed |
| Edit Booking | Changes saved | ✔ Passed |
| Delete Booking | Booking removed | ✔ Passed |
| Overlap Validation | Overlapping booking rejected | ✔ Passed |
| Date Validation | End date must be after start | ✔ Passed |

---

### ✔ Validation Testing

#### **End Date Validation**
- Start: 10 Jun  
- End: 9 Jun  
→ ❌ Rejected

#### **Overlap Validation**
Existing: 10–15 Jun  
New: 14–20 Jun  
→ ❌ Rejected

#### **Non‑Overlap**
Existing: 10–15 Jun  
New: 16–20 Jun  
→ ✔ Accepted

---

### ✔ Code Validation
- Python code validated with no syntax errors  
- Django templates render without issues  
- Forms validated correctly  
- URLs resolve correctly  

---

### ✔ Browser Testing
Tested on:
- Chrome  
- Firefox  
- Edge  
- Mobile Android

All pages responsive and functional.


## Code Validation
- No Python syntax errors  
- Templates render correctly  
- Forms validate correctly  
- URLs resolve correctly  

## Lighthouse Report

Lighthouse audits were run on the deployed site to ensure performance, accessibility, best practices, and SEO.

### Desktop Results

| Category       | Score |
|----------------|-------|
| Performance    | 95%   |
| Accessibility  | 100%  |
| Best Practices | 100%  |
| SEO            | 100%  |

### Mobile Results

| Category       | Score |
|----------------|-------|
| Performance    | 85%   |
| Accessibility  | 100%  |
| Best Practices | 100%  |
| SEO            | 100%  |


### Notes
- Performance may vary depending on network conditions.
- Accessibility score benefits from semantic HTML and proper labels.
- Best Practices and SEO are strong due to clean structure and metadata.

Screenshots of the Lighthouse reports can be added here if required by assessors.


## Deployment

### Heroku Deployment Steps

1. **Create Heroku App**
   - Log into Heroku
   - Create new app
   - Select region: Europe

2. **Add Buildpacks**
   - Python
   - NodeJS (optional)

3. **Set Environment Variables**
   In Heroku → Settings → Config Vars:

   ```
   SECRET_KEY=your_secret_key
   DEBUG=False
   ALLOWED_HOSTS=yourapp.herokuapp.com
   ```

4. **Install Requirements**
   ```
   pip3 install -r requirements.txt
   ```

5. **Collect Static Files**
   ```
   python3 manage.py collectstatic
   ```

6. **Push to Heroku**
   ```
   git push heroku main
   ```

7. **Open App**
   ```
   heroku open
   ```

---

### Local Deployment

1. Clone repository  
2. Create virtual environment  
3. Install dependencies  
4. Run migrations  
5. Start server  

```
python3 manage.py runserver
```


## Future Enhancements

### ⭐ Sitter Availability System
Allow sitters to define available dates and automatically match bookings to available sitters.

### ⭐ Payment Integration
Add Stripe or PayPal to allow users to pay for bookings online.

### ⭐ Pet Profiles
Upload pet photos and additional details.

### ⭐ Booking Calendar View
Display bookings in a calendar layout for easier visualization.

### ⭐ Email Notifications
Send confirmation emails when bookings are created, updated, or cancelled.

### ⭐ Reviews & Ratings
Allow users to rate sitters after a completed booking.

### ⭐ Admin Dashboard
Provide analytics and management tools for site administrators.

## Credits & Acknowledgements

- Django documentation — for framework guidance 
- Bootstrap 5 — for responsive UI components 
- Code Institute walkthroughs, project structure and assessment criteria   
- Special thanks to **Copilot** for guidance during development, for assistance with debugging, validation logic, and documentation.  

## Code Authorship

All code in this project was written by me. I used documentation,
tutorials, and guidance from Code Institute > "Developing with Django" to learn Django, but I typed, adapted,
and understood every line myself. No code was copied from other
projects or repositories.
