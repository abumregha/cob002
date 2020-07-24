from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class NewAccountDataForm(ModelForm):
    class Meta:
        model = NewAccountData
        exclude = ('status', 'user')
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)