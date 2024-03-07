from django.db import models
class Contact(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_num = models.CharField(max_length=10)
    comments=models.CharField(max_length=400,default='')#if you forgot to add any field and then #you will release that i want that field in my model and admin then you have to add
    #default='' with in the field like comments field
     
# Create your models here.
