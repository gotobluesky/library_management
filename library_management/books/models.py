from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    page_count = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Loan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loaned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.book}'
