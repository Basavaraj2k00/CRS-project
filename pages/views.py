from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from listings.models import Listing
from realtors.models import Owner

from listings.choices import bedroom_choices, price_choices, type_choices

# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'type_choices': type_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all owners
    owners = Owner.objects.order_by('-hire_date')[:3]

    # Get MVP

    mvp_owners = Owner.objects.all().filter(is_mvp=True)

    context = {
        'owners': owners,
        'mvp_owners': mvp_owners

    }
    return render(request, 'pages/about.html', context)
