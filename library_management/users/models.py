from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add your custom fields here
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    USER_ROLE_CHOICES = (
        (0, 'Admin'),
        (1, 'User'),
        (2, 'Guest'),
    )
    user_role = models.IntegerField(choices=USER_ROLE_CHOICES, default=2)