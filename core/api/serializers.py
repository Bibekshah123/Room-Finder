from rest_framework import serializers
from rooms.models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'title', 'description', 'location', 'price']
        
        
# class Booking(serializers.ModelSerializer):
#     class Meta:
#         models = Booking
#         fields = ['id', ]