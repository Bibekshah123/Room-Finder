from django.urls import path
from .views import *

urlpatterns = [
    path('room-list/', RoomListApiView.as_view()),
    
    #auth
    
]
