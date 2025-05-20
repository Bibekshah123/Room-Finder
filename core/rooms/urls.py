from django.urls import path
from .views import *

urlpatterns = [
        #login
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('', RoomListView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('room/add/', RoomCreateView.as_view(), name='room_add'),
    path('room/<int:pk>/edit/', RoomUpdateView.as_view(), name='room_edit'),
    path('room/<int:pk>/delete/', RoomDeleteView.as_view(), name='room_delete'),
    path('booking/', BookingCreateView.as_view(), name='booking_add'),
]