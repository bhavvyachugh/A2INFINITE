from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

def validate_mobile(mobile_num):
    mobile_num = mobile_num.replace(' ', '')

    if len(mobile_num) < 10 or len(mobile_num) > 15:
        raise ValidationError("Mobile number not valid")


class User(AbstractUser):
    school_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    email = models.EmailField('email address',unique=True)
    phone = models.CharField(max_length=12)
    country = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    city =models.CharField(max_length=120)
    pin_code = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class UserActivity(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    session_key = models.CharField(max_length=40, db_index=True)
    login = models.DateTimeField(auto_now_add=True)
    logout = models.DateTimeField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch.dispatcher import receiver
from django.db.models.functions import Now

@receiver(user_logged_in)
def register_login(sender, user, request, **kwargs):
    UserActivity.objects.create(
        user=user,
        session_key=request.session.session_key
    )

@receiver(user_logged_out)
def register_logout(sender, user, request, **kwargs):
    UserActivity.objects.filter(
        user=user,
        session_key=request.session.session_key
    ).update(
        logout=Now()
    )        
