from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [

    path("admin-login/", auth_views.LoginView.as_view(template_name="dashboard/login.html"), name="dashboard-login"),
    path("admin-logout/", auth_views.LogoutView.as_view(next_page="login"), name="dashboard-logout"),

    
    path('', DashboardHomeView.as_view(), name='dashboard_home'),
    path('rooms/', DashboardRoomsView.as_view(), name='dashboard_rooms'),
    path('room/create/', DashboardRoomCreate.as_view(), name='dashboard_room_create'),
    path('rooms/edit/<int:pk>/', DashboardRoomUpdateView.as_view(), name='dashboard_room_edit'),
    path('rooms/delete/<int:pk>/', DashboardRoomDeleteView.as_view(), name='dashboard_room_delete'),
    
    path('bookings/', DashboardBookingsView.as_view(), name='dashboard_bookings'),
    path('users/', DashboardUsersView.as_view(), name='dashboard_users'),
]
