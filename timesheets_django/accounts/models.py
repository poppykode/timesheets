from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    DES = (
        ('management','Management'),
        ('employee','Employee'),
    )
    first_name =models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    is_management = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    designation = models.CharField(max_length=20,choices=DES)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ["-date_joined", ]