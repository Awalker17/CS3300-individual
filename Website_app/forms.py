from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ShowForm(ModelForm):
   class Meta:
      model = Show
      fields =["title", "finished", "season", "episode", "language", "streaming", "description", "synopis"]
      
class RegisterForm(UserCreationForm):
   email = forms.EmailField(required = True)
   class Meta:
      model = User
      fields =["username", "email", "password1", "password2"]

