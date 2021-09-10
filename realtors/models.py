from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    photo = models.ImageField(default='default.jpg',null=True,blank=True,upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=200,)
    phone = models.CharField(max_length=200,null=True,blank=True,)
    is_mvp = models.BooleanField(default=False,null=True,blank=True)
    hire_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name
    



































