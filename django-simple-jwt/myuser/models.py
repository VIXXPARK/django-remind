from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManger

class User(AbstractUser):
    username=models.CharField(unique=True,max_length=25)
    email=models.EmailField(unique=True)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']

    objects=UserManger()

    def __str__(self):
        return self.username