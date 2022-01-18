from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField()
    objects = models.Manager()

    def __repr__(self):
        return f'id: {self.id}::{self.title}::{self.content[:5]}'
