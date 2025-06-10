from django import forms
from rooms.models import *

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ['owner']
        labels = {
            'title': 'Room Title',
            'description': 'Room Description',
            'location': 'Room Location',
            'price': 'Monthly Rent',
            'image': 'Upload Image',
        }
        help_texts = {
            'image': 'Upload a clear image of the room.',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter room title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the room...',
                'rows': 4
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City or area'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 500'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }