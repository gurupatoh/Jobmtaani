from django.contrib.auth.models import User
from .models import Placement
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomClientForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = '__all__'

