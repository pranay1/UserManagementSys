from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=254, default='')
    phone = models.CharField(max_length=12, default='')
    address = models.CharField(max_length=200, default='')
    profession = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=12, default='')
    state = models.CharField(max_length=12, default='')
    country = models.CharField(max_length=12, default='')
    dob = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{}'.format(self.username)
