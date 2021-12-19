from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManger(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set.')
        email = self.normalize_email(email)
        user = Account()
        user.set_email(email)
        user.username = username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, username, password, **extra_fields)


class Account(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManger()

    def set_email(self, email):
        self.email = email

    def __repr__(self):
        return f'아이디: {self.id}, 이름 : {self.username}, 이메일: {self.email}'
