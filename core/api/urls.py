from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    #auth
    # Djoser default auth endpoints (registration, password reset, etc.)
    path('auth/', include('djoser.urls')),
    # Djoser JWT endpoints (login, logout, token refresh)
    path('auth/', include('djoser.urls.jwt')),

    
    path('rooms/', RoomListApiView.as_view()),
    path('roomdetail/<int:pk>/', RoomDetailApiview.as_view()),
    
    path('bookings/', BookingApiView.as_view()),
    path('bookingsdetail/<int:pk>/', BookingDetailApiView.as_view()),
    
]





