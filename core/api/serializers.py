from rest_framework import serializers
from rooms.models import *
# from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password']


class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['owner']
        
        

class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    
    class Meta:
        model = Booking           
        fields = '__all__' 