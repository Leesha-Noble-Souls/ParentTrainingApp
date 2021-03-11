from django.db import models
from dashboard.models import Parent

VISIBLE = True
DONE = True
RECEIVED = True

class LessonPlan(models.Model):
    topic = models.CharField(max_length = 200)
    aim = models.CharField(max_length = 200, default = "Aim:")
    objectives = models.TextField(null = True)
    activity = models.TextField()
    link = models.URLField(null = True)
    # visibility = models.BooleanField(default = not VISIBLE)
    # lesson_status = models.BooleanField(default = not DONE)
    # feedback_status = models.BooleanField(default = not RECEIVED)
    assigned_users = models.ManyToManyField(Parent)

    def __str__(self):
        return self.topic
