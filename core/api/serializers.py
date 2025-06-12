from rest_framework import serializers
from rooms.models import *
# from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id', 'username', 'email', 'password', 're_password')

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'username', 'password']
    
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']
        
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password']


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