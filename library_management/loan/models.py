from django.db import models

# Create your models here.
class Loan(models.Model):
    userid = models.IntegerField()
    book_id = models.IntegerField()
    loan_time = models.DateField()
    loan_period = models.IntegerField()
