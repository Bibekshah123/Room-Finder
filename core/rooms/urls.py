from django.urls import path
from .views import *

urlpatterns = [
        #login
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('', HomeView.as_view(), name='home'),
    path('room/', RoomListView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('room/add/', RoomCreateView.as_view(), name='room_add'),
    path('room/<int:pk>/edit/', RoomUpdateView.as_view(), name='room_edit'),
    path('room/<int:pk>/delete/', RoomDeleteView.as_view(), name='room_delete'),
    path('booking/', BookingCreateView.as_view(), name='booking_add'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', contact_view, name='contact'),
    
    path('book/', BookRoomView.as_view(), name='booking'),
    path('my-bookings/', MyBookingsView.as_view(), name='my_bookings'),
]