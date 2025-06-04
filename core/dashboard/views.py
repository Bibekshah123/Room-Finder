from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from rooms.models import Room, Booking

class DashboardHomeView(TemplateView):
    template_name = 'dashboard/home.html'

class DashboardRoomsView(ListView):
    model = Room
    template_name = 'dashboard/rooms.html'
    context_object_name = 'rooms'

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
