from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing

from listings.choices import bedroom_choices, price_choices, type_choices

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,

    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if 'keywords':
            queryset_list = queryset_list.filter(description__icontains=keywords)

    #Area
    if 'area' in request.GET:
        area = request.GET['area']
        if 'area':
            queryset_list = queryset_list.filter(area__icontains=area)


  #TYPE
    if 'type' in request.GET:
        type = request.GET['type']
        if 'type':
            queryset_list = queryset_list.filter(type__icontains=type)
    
    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if 'bedrooms':
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms) 

    #Bedrooms
    if 'price' in request.GET:
        price = request.GET['price']
        if 'price':
            queryset_list = queryset_list.filter(price__lte=price) #lte for less than equals to

    context = {
        'listings' : queryset_list,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'type_choices': type_choices,
        'values': request.GET,
    }

    return render(request, 'listings/search.html', context)
