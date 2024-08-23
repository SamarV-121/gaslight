from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    full_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    address = models.TextField()
