from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import BooleanField


class User(AbstractUser):
    is_email_verified = models.BooleanField(default= False)

    def __str__(self):
        return self.email
        