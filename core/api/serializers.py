from rest_framework import serializers
from rooms.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['owner']
        
        

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    
    class Meta:
        model = Booking           
        fields = '__all__' 