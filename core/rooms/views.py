from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views import View

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
                return redirect('room_list')
        return render(request, 'registration/login.html', {'form': form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('room_list')

    
    
class RoomListView(ListView):
    model = Room
    template_name = 'room_list.html'
    
class RoomCreateView( CreateView):
    model = Room
    template_name = 'room_create.html'
    form_class = RoomForm
    success_url = reverse_lazy('room_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    


class RoomDetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'
    
class RoomUpdateView(UpdateView):
    model = Room
    template_name = 'room_update.html'
    form_class = RoomForm
    success_url = reverse_lazy('room_list')
    
    def test_func(self):
        return self.get_object().owner == self.request.user
    
class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'room_delete.html'
    success_url = reverse_lazy('room_list')
    
    def test_func(self):
        return self.get_object().owner == self.request.user
    
    
class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = reverse_lazy('room_list')

    def form_valid(self, form):
        form.instance.renter = self.request.user
        room = form.cleaned_data['room']
        room.available = False
        room.save()
        return super().form_valid(form)

    
    