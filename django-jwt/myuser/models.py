from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
import uuid

def make_uuid():
    return str(uuid.uuid4())

class User(AbstractUser):
    username=None
    id=models.CharField(editable=False,max_length=36,db_index=True,unique=True,default=make_uuid,primary_key=True)
    email=models.EmailField(_('email address'),unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserManager()

    def __str__(self):
        return self.email