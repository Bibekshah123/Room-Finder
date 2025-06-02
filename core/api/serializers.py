from rest_framework import serializers
from rooms.models import *

class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'title', 'description', 'location', 'price']
        
class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'title', 'description', 'location', 'price', 'image']
        
        
# class Booking(serializers.ModelSerializer):
#     class Meta:
#         models = Booking
#         fields = ['id', ]