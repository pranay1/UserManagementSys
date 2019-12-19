from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from auth0login.models import Profile
from django.conf import settings
import datetime


# Create your models here.

class Device(models.Model):
    # profile = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)
    # username = models.CharField(profile.username)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)
    # id = models.IntegerField(primary_key=True)

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, default='Pass List here')
    parameters = models.CharField(max_length=1000, default='Pass dictionary here')
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)

    # price = models.DecimalField(max_digits=9, decimal_places=2, default=0)  # default=Decimal('0.0000')
    # quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
