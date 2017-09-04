from django.db import models


# Create your models here.
class Device(models.Model):
    custom_id = models.CharField(max_length=1024)


class Point(models.Model):
    device = models.CharField(max_length=1024)
    longitude = models.CharField(max_length=1024)
    latitude = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
