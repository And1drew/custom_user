from django.db import models
from django.contrib.auth.models import AbstractUser


class My_User (AbstractUser):
    user_name = models.CharField(default='', max_length=50)
    password = models.CharField(default='', max_length=50)
