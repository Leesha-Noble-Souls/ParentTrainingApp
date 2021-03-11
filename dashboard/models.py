from django.contrib.auth.models import AbstractUser
from django.db import models

from lessonPlans.models import LessonPlan

class Parent(AbstractUser):

    def __str__(self):
        return self.username
