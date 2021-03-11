from django.contrib.auth.models import AbstractUser
from django.db import models

class Parent(AbstractUser):

    def __str__(self):
        return self.username
