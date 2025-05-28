from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from rooms.models import Room
# Create your views here.


class RoomListApiView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    
class RoomCreateApiView(generics.CreateAPIView):
    pass
    