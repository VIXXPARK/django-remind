from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import Account


class LogType(models.TextChoices):
    LOGIN = 'login', _('LOGIN'),    # NAME / VALUE / LABEL
    LOGOUT = 'logout', _('LOGOUT')

    @staticmethod
    def index_to_type(index):
        if index == 0:
            return LogType.LOGIN
        else:
            return LogType.LOGOUT


class Log(models.Model):
    account = models.ForeignKey(Account, related_name='logs', null=True, on_delete=models.CASCADE)
    model_type = models.CharField(max_length=20, choices=LogType.choices, default=LogType.LOGIN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __repr__(self):
        return f'model_type: {self.model_type}'
