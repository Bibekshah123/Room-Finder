from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    #auth
    path('', Home.as_view()),
    path('users/', UserApiView.as_view()),
    path('register/', RegisterApiView.as_view()),
    
    path('rooms/', RoomListApiView.as_view()),
    path('roomdetail/<int:pk>/', RoomDetailApiview.as_view()),
    
    path('bookings/', BookingApiView.as_view()),
    path('bookingsdetail/<int:pk>/', BookingDetailApiView.as_view()),
]





