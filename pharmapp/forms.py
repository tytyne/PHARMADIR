from django import forms
from django.contrib.auth.models import User
from .models import Pharmacy,Request,





class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
     