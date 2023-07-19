from django.db import models

# Create your models here.

class Vendor(models.Model):

    name=models.CharField(max_length=33)
    email=models.CharField
    image=models.ImageField
    phone_number=models.CharField(max_length=10)
    date_created=models.DateTimeField(max_length=10)
