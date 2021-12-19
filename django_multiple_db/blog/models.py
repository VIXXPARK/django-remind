from django.db import models

from account.models import Account


class Blog(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __repr__(self):
        return f'title : {self.title}'
