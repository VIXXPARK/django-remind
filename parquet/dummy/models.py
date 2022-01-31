from django.db import models


class Dummy(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    is_delete = models.BooleanField(default=False)
    objects = models.Manager()
