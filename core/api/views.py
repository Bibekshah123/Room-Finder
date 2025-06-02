from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomListSerializer, RoomCreateSerializer
from rooms.models import Room
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    # permission_classes = [IsAuthenticated]


# class RoomListApiView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Room.objects.all()
#     serializer_class = RoomListSerializer
    
    
# class RoomCreateApiView(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = RoomCreateSerializer
    