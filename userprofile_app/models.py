from django.db import models
from django.contrib.auth.models import User
import datetime


def user_directory_path(instance, filename):
    """
    Returns Filepath where instance provides the user.id and filename
    the name of provided data
    - `instance`: instance.user.id
    - `filename`: name of data
    """
    return f'user/{instance.user.id}/{filename}'

# Create your models here.


class Profile(models.Model):
    TYPE_CHOICES = {
        'business': 'business',
        'customer': 'customer'
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    file = models.FileField(upload_to=user_directory_path, blank=True)
    location = models.CharField(max_length=50, blank=True)
    tel = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=50, blank=True)
    working_hours = models.CharField(max_length=50, blank=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
