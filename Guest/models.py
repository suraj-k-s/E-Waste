from django.db import models
from Adminstrator.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")
    


class tbl_company(models.Model):
    cmp_name=models.CharField(max_length=50)
    cmp_contact=models.CharField(max_length=50)
    cmp_email=models.CharField(max_length=50)
    cmp_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    cmp_photo = models.FileField(upload_to='Assets/cmpPhoto/')
    cmp_proof = models.FileField(upload_to='Assets/cmpProof/')
    cmp_status = models.IntegerField(default="0")