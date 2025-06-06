from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('rooms/', RoomListApiView.as_view()),
    path('roomdetail/<int:pk>/', RoomDetailApiview.as_view()),
    
    path('bookings/', BookingApiView.as_view()),
    path('bookings/detail/<int:pk>/', BookingDetailApiView.as_view()),
]





