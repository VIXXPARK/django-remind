from django.db import models


class Account(models.Model):
    name = models.CharField(blank=True, max_length=30)
    objects = models.Manager()
