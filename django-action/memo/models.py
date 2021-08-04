from django.db import models


class Memo(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.title
