from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from realtors.models import Owner



class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fileds = "__all__"
        exclude = ['user','is_mvp','hire_date']
        