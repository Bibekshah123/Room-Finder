from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer, BookingSerializer
from rooms.models import Room, Booking
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# Create your views here.

class RoomListApiView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class RoomDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer    

class BookingApiView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class BookingDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
    
# class BookingViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = BookingSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
        
        













# class RoomListApiView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Room.objects.all()
#     serializer_class = RoomListSerializer
    
    
# class RoomCreateApiView(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = RoomCreateSerializer
    