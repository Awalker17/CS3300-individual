from django.forms import ModelForm
from .models import *

class ShowForm(ModelForm):
     class Meta:
        model = Show
        fields ='__all__'

class UserForm(ModelForm):
     class Meta:
        model = User
        fields ='__all__'