# books/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    USER_ROLE_CHOICES = (
        (0, 'Admin'),
        (1, 'User'),
        (2, 'Guest'),
    )
    user_role = models.IntegerField(choices=USER_ROLE_CHOICES, default=2)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)  # Fixes SystemCheckError
    # Other fields...

    def __str__(self):
        return self.title