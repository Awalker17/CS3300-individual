from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class ShowForm(ModelForm):
   class Meta:
      model = Show
      fields ='__all__'

class UserForm(ModelForm):
   class Meta:
      model = User
      fields ='__all__'
      
class RegisterForm(UserCreationForm):
   email = forms.EmailField(required = True)
   class Meta:
      model = User
      fields =["username", "email", "password1", "password2"]

