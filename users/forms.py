from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile



class registerUser(UserCreationForm):
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=254)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name' ,'last_name', 'username', 'email', 'password1', 'password2']

class addProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
