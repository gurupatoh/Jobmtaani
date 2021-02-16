from .models import Placement, Client,User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction


# generate form for user
class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields =['user_name','user_email','user_location']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_user = True
        if commit:
            user.save()
            return user


# generate from for client
class ClientRegisterForm(UserCreationForm):

    class Meta:
        model = Client
        fields = '__all__'

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_client = True
            if commit:
                user.save()
                return user


# form for adding a new job placement
class CustomClientForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = ['placement_title', 'placement_slug', 'placement_location', 'placement_quote',
                  'placement_description', 'placement_category']
