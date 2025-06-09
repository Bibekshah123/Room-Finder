from django.urls import path
from .views import *


urlpatterns = [
    path('', DashboardHomeView.as_view(), name='dashboard_home'),
    path('rooms/', DashboardRoomsView.as_view(), name='dashboard_rooms'),
    path('rooms/edit/<int:pk>/', DashboardRoomUpdateView.as_view(), name='dashboard_room_edit'),
    path('rooms/delete/<int:pk>/', DashboardRoomDeleteView.as_view(), name='dashboard_room_delete'),
    path('bookings/', DashboardBookingsView.as_view(), name='dashboard_bookings'),
    path('users/', DashboardUsersView.as_view(), name='dashboard_users'),
]
