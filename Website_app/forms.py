from django.forms import ModelForm
from .models import *

class ShowForm(ModelForm):
     class Meta:
        model = Show
        fields =('title', 'description')