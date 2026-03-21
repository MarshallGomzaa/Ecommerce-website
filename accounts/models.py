from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=15, default="+977")
    address = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.username