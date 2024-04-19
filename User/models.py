from django.db import models
from Guest.models import *



class tbl_request(models.Model):
    request_date=models.DateField()
    request_amount=models.IntegerField()
    request_status=models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    company = models.ForeignKey(tbl_company, on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=100)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_details=models.CharField(max_length=1000)
    complaint_staus=models.IntegerField(default="0")
    
    complaint_reply=models.CharField(max_length=1000)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_title=models.CharField(max_length=100)
    feedback_date=models.DateField(auto_now_add=True)
    feedback_details=models.CharField(max_length=1000)