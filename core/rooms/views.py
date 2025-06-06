from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models import Q

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'registration/login.html', {'form': form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('room_list')

# @method_decorator(cache_page(60 * 15), name='dispatch')
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
# @method_decorator(cache_page(60 * 15), name='dispatch') 
class RoomListView(ListView):
    paginate_by = 6
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'rooms'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        rooms = Room.objects.all()
        if query:
            rooms = rooms.filter(
                Q(title__icontains=query) | Q(location__icontains=query)
            )
        return rooms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
    
class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    template_name = 'room_create.html'
    form_class = RoomForm
    success_url = reverse_lazy('room_list')
    context_object_name = 'rooms'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
# @method_decorator(cache_page(60 * 15), name='dispatch')
class RoomDetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'
    context_object_name = 'rooms'
    
    
class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Room
    template_name = 'room_update.html'
    form_class = RoomForm
    success_url = reverse_lazy('room_list')
    context_object_name = 'rooms'
    
    def test_func(self):
        return self.get_object().owner == self.request.user
    
class RoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Room
    template_name = 'room_delete.html'
    success_url = reverse_lazy('room_list')
    context_object_name = 'rooms'
    
    def test_func(self):
        return self.get_object().owner == self.request.user
    
    
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = reverse_lazy('room_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        room = form.cleaned_data['room']
        room.available = False
        room.save()
        return super().form_valid(form)

class AboutPageView(TemplateView):
    model = About
    template_name = "about.html"
    success_url = reverse_lazy('room_list')


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('room_list') 

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thank you for contacting us! We'll get back to you soon.")
        return super().form_valid(form)
    

    
@method_decorator(login_required, name='dispatch')
class BookRoomView(View):
    def post(self, request):
        room_id = request.POST.get('room')
        room = get_object_or_404(Room, pk=room_id)

        # prevent self-booking
        if room.owner == request.user:
            messages.error(request, "You cannot book your own room.")
            return redirect('room_detail', pk=room_id)

        # check if room is already booked by anyone
        if Booking.objects.filter(room=room).exists():
            messages.error(request, "This room has already been booked.")
            return redirect('room_detail', pk=room_id)

        # Book the room
        Booking.objects.create(user=request.user, room=room)
        messages.success(request, "Room booked successfully!")
        return redirect('my_bookings')

        


class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'mybookings.html' 
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)