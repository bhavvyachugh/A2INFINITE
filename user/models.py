from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=12)
    country = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    district = models.CharField(max_length=122)
    city = models.CharField(max_length=122)

    def __str__(self):
        return self.username