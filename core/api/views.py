from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer, BookingSerializer, UserSerializer, RegisterSerializer
from rooms.models import Room, Booking
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, permissions
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {'message': 'Hello Bikki!!!'}
        return Response(content)

class UserApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class RoomListApiView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner', 'location', 'price']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class RoomDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class BookingApiView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    
class BookingDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
  
    
  
    
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
    