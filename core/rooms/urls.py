from django.urls import path
from .views import *

urlpatterns = [
    #login
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('profile/', ProfileView.as_view(), name='profile'),
    
    path('', HomeView.as_view(), name='home'),
    path('room/', RoomListView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('room/add/', RoomCreateView.as_view(), name='room_add'),
    path('room/<int:pk>/edit/', RoomUpdateView.as_view(), name='room_edit'),
    path('room/<int:pk>/delete/', RoomDeleteView.as_view(), name='room_delete'),
    
    path('booking/', BookingCreateView.as_view(), name='booking_add'),
    path('bookings/', BookingsView.as_view(), name='bookings'),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('booking/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
    
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    
    path('book/', BookRoomView.as_view(), name='booking'),
    
    path('activate/<uid>/<token>/', activate_account, name='activate'),

]