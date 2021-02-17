from .models import Placement, Client,CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from django.forms import ModelForm



# generate form for user
class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields =['username','first_name','last_name','email','user_location']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_user = True
        if commit:
            user.save()
            return user


# generate from for client
class ClientRegisterForm(ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)
        Confirmpassword = forms.CharField(widget=forms.PasswordInput)

        class Meta:
            model = Client
            fields =['client_name','client_location','client_description','password','Confirmpassword']

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
