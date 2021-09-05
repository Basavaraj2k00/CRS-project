from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):



    context = {

    }

    return render(request,'listings/listing.html',context)

def search(request):



    context = {

    }

    return render(request,'listings/listings.html',context)