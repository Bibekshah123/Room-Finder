from django.urls import path
from .views import DashboardHomeView, DashboardRoomsView, DashboardBookingsView, DashboardUsersView

urlpatterns = [
    path('', DashboardHomeView.as_view(), name='dashboard_home'),
    path('rooms/', DashboardRoomsView.as_view(), name='dashboard_rooms'),
    path('bookings/', DashboardBookingsView.as_view(), name='dashboard_bookings'),
    path('users/', DashboardUsersView.as_view(), name='dashboard_users'),
]
