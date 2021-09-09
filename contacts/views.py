from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import Group
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == "POST":
        listing_id = request.POST.get("listing_id")
        listing = request.POST.get("listing")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        user_id = request.POST.get("user_id")
        owner_email = request.POST.get("owner_email")
        user_name = request.POST.get("username")

        # check if the user made inquery already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for ths listing.")
                return redirect('/listings/'+listing_id+"/")

        contact = Contact(user_name=user_name, listing_id=listing_id, listing=listing,
                          name=name, phone=phone, message=message, user_id=user_id, email=email)
        contact.save()
        # send mail
        try:
            send_mail(
                'House Listing Inquiry',
                f'\nGreetings from CITY RENTAL SERVICES\n\n\nThere has been an inquiry for {listing} from {user_name} & We request you to get back to them as soon as possible!.\n\nTheir message:\n {message}\n\nThier contact details are:\n\nEmail: {email}\nPhone: {phone}\n\n\nThank You.\n',
                'contactcityrentalservices@gmail.com',
                [owner_email, 'yr2327yr@gmail.com'],
                fail_silently=False
            )
        except:
            messages.error(
            request, f"There has been an error for sending the owner an email, Please contact us")

        messages.success(
            request, f"Your request has been submitted, the house owner will get back to you soon.")

    return redirect('/listings/'+listing_id+"/")
