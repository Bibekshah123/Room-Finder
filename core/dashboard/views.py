from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, DetailView
from django.contrib.auth.models import User
from rooms.models import Room, Booking
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"
    login_url = "login"  # URL name for login page

class AdminRoomListView(LoginRequiredMixin, ListView):
    model = Room
    template_name = "dashboard/dashboard_rooms.html"
    context_object_name = "rooms"
    login_url = "login"

class DashboardHomeView(TemplateView):
    template_name = 'dashboard/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_rooms'] = Room.objects.count()
        context['total_bookings'] = Booking.objects.count()
        context['total_users'] = User.objects.count()
        return context

class DashboardRoomsView(ListView):
    model = Room
    template_name = 'dashboard/dashboard_rooms.html'
    context_object_name = 'rooms'

class DashboardRoomCreate(CreateView):
    model = Room
    template_name = 'dashboard/dashboard_room_create.html'
    form_class = RoomForm

    
class DashboardRoomUpdateView(UpdateView):
    model = Room
    fields = ['title', 'description', 'location', 'price', 'image']
    template_name = 'dashboard/dashboard_room_edit.html'
    success_url = reverse_lazy('dashboard_rooms')
    
class DashboardRoomDeleteView(DeleteView):
    model = Room
    template_name = 'dashboard/dashboard_room_delete.html'
    success_url = reverse_lazy('dashboard_rooms')

class DashboardBookingsView(ListView):
    model = Booking
    template_name = 'dashboard/bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.select_related('room', 'user')

class DashboardUsersView(ListView):
    model = User
    template_name = 'dashboard/users.html'
    context_object_name = 'users'
