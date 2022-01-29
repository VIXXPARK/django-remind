from django.db import models

from account.models import Account


class Issue(models.Model):
    # class Meta:
    #     indexes = [
    #         models.Index(fields=['model_type', 'is_complete', 'id'], name='issue_type_complete_id'),
    #     ]

    model_type = models.IntegerField(default=1)
    is_complete = models.BooleanField(default=False)
    account = models.ForeignKey(Account, null=True, related_name='issues', on_delete=models.CASCADE)
    objects = models.Manager()
