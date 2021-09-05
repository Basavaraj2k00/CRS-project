from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Owner
from listings.models import Listing


# Create your views here.
def index(request):
    context = {

    }

    return render(request, 'pages/index.html', context)


def about(request):

    context = {

    }
    return render(request, 'pages/about.html', context)
