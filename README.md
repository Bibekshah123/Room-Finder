# 🏠 Room Finder App

The **Room Finder App** is a full-stack Django web application that helps users find, book, and manage rental rooms. It features secure authentication (djoser + JWT), room listings, owner dashboards, booking functionality, and role-based access.

---

## 🔧 Tech Stack

### 🖥 Frontend:
- Django Templates (HTML, CSS, Bootstrap)
- Template-based rendering with Django context

### ⚙️ Backend:
- Django
- Django REST Framework (DRF)
- Djoser (JWT Authentication)
- Custom User Model
- SQLite

---

## 🚀 Features

### ✅ User Authentication (via Djoser + JWT)
- Register with email verification
- Login & Logout
- Token-based authentication using JWT
- Custom user model with email as primary field

### 🛏 Room Management
- Owners can add/edit/delete rooms
- Users can view all available rooms
- Room detail pages
- Conditional logic: Only owners can edit/delete, renters can book

### 📅 Booking System
- Users can book available rooms
- Already booked rooms show "unavailable" message
- Only authenticated users can book
- Duplicate bookings prevented

### 🧠 Backend API (DRF)
- RESTful APIs for rooms and bookings
- Authentication endpoints via Djoser
- Role-based permissions for owners and users
- Token refresh, blacklisting, and logout

### 🌐 Pages
- Home
- Room List
- Room Detail
- Register
- Login
- Dashboard (for owners)

---
## ⚙️ Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/Bibekshah123/Room-Finder.git
cd core

2. Install Dependencies
```bash
pip install -r requirements.txt

3. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate

4. Create Superuser
```bash
python manage.py createsuperuser

5. Run Server
```bash
python manage.py runserver

---

## 🛡️ Authentication Endpoints (via Djoser)
Endpoint	                            Purpose
/api/auth/users/	                    Register
/api/auth/jwt/create/	                    Login
/api/auth/jwt/refresh/	                    Refresh JWT
/api/auth/users/activation/	            Email activation
/api/auth/users/me/	                    Get current user





