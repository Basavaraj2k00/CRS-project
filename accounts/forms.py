from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from realtors.models import Owner
from listings.models import Listing


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fileds = "__all__"
        exclude = ['user','is_mvp','hire_date']
        

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        filed = "__all__"
        exclude = ['owner','is_published','list_date']
