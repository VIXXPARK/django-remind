from django.db import models

from account.models import Account
from issue.models import Issue


class Work(models.Model):
    issue = models.ForeignKey(Issue, related_name='works', null=True, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name='works', null=True, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    model_type = models.IntegerField(default=1)

    objects = models.Manager()
