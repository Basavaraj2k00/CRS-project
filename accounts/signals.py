from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from realtors.models import Owner
from listings.models import Listing


def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='owner')
        instance.groups.add(group)
        Owner.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
        )
        print('Profile created!')


post_save.connect(customer_profile, sender=User)

# def listing(sender, instance, created, **kwargs):
#     if created:
#         Listing.objects.create(
#             user=instance,
#             description=instance.description,
#         )
#         print('Listing created!')


# post_save.connect(listing, sender=Owner)