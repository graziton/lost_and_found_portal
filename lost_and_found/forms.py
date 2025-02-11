from django import forms
from .models import LostItem, FoundItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['title', 'description', 'location', 'image']
        # The date_reported and status are automatically managed

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['title', 'description', 'location', 'image']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
