from django.db import models
from myuser.models import User


class Blog(models.Model):
    title = models.CharField(max_length=128)
    userId = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return self.title
