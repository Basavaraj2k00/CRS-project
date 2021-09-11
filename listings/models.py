from django.db import models
from datetime import datetime
from realtors.models import Owner
# Create your models here.
class Listing(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,)
    Choices = (('BHK','BHK'),('PG','PG'),('Single Room','Single Room'))
    type = models.CharField(max_length=200,choices=Choices,null=True)
    address = models.TextField(blank=True)
    map_url = models.URLField(help_text = "GoogleMap location of the house.",blank=True)

    city = models.CharField(max_length=200,)
    area = models.CharField(max_length=200,null=True)

    zipcode = models.CharField(max_length=200,)
    description = models.TextField(blank=True)

    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)

    is_published = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now,blank=True)


    def __str__(self):
        return self.title
    



