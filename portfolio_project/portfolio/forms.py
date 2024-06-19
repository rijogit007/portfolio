from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Portfolio
from django.contrib.auth.models import User

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description','image']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]
        widgets = {
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'password':forms.PasswordInput(attrs={'class':'form-control'})
                } 