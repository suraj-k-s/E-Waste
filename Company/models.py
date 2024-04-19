from django.db import models
from Company.models import *
from Adminstrator.models import *
from User.models import *


class tbl_waste(models.Model):
    category = models.ForeignKey(tbl_Category, on_delete=models.CASCADE)
    waste_quantity=models.IntegerField()
    request = models.ForeignKey(tbl_request, on_delete=models.CASCADE)