from django.urls import path
from .views import *
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('room', views.RoomViewSet, basename='rooms')

urlpatterns = [
    # path('room-list/', RoomListApiView.as_view()),
    # path('room-add/', RoomCreateApiView.as_view()),
    
    
    #auth
    
] + router.urls



