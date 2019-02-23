from django.db import models
import uuid

# Create your models here.
class Wine(models.Model):
    ID = models.IntegerField(primary_key = True)
    COUNTRY = models.CharField(max_length = 30)
    DESCRIPTION = models.CharField(max_length = 500)
    DESIGNATION = models.CharField(max_length = 100)
    POINTS = models.IntegerField(default=0)
    PRICE = models.IntegerField(default=0)
    PROVINCE = models.CharField(max_length = 50)
    REGION_1 = models.CharField(max_length=100)
    REGION_2 = models.CharField(max_length=100)
    VARIETY = models.CharField(max_length=100)
    WINERY = models.CharField(max_length=100)
