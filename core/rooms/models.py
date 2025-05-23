from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_rooms')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"{self.user.username} booked {self.room.title}"