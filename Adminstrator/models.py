from django.db import models
from Adminstrator.models import *

# Create your models here.

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)


class tbl_Category(models.Model):
    Category_name=models.CharField(max_length=50)

class tbl_adminregistration(models.Model):
    AdminRegistration_name=models.CharField(max_length=50)
    AdminRegistration_contact=models.CharField(max_length=50)
    AdminRegistration_email=models.CharField(max_length=50)
    AdminRegistration_password=models.CharField(max_length=50)

 


class tbl_ewaste(models.Model):
    ewaste_name=models.CharField(max_length=50)
    ewaste_details=models.CharField(max_length=50)
    ewaste_price=models.CharField(max_length=50)
    ewaste_photo = models.FileField(upload_to='Assets/EwastePhoto/')
    
class tbl_reply(models.Model):
    reply_name=models.CharField(max_length=1000)





