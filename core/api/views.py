from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomListSerializer
from rooms.models import Room
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class RoomListApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    
    
class RoomCreateApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        pass
    
    