from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30,null = True)
    last_name = models.CharField(max_length=30,null = True)
    address = models.CharField(max_length=500,null = True)
    dob= models.DateField(null = True)
    status = models.IntegerField(null = True)
    email = models.EmailField(max_length=254,null = True)
    phone = models.CharField(max_length=25,blank=True, help_text='Contact phone number',null = True)
    created = models.DateTimeField(auto_now_add=True,null = True)
    updated = models.DateTimeField(auto_now=True,null = True)
