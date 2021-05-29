from django.db import models
from dashboard.models import Parent

VISIBLE = True

class Topic(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField()
    parent_topic = models.ForeignKey('self', null=True, blank=True, related_name='parentTopic', on_delete=models.CASCADE)
    # related_name: The name to use for the relation from the related object back to this one.

    def __str__(self):
        return self.name


class LessonPlan(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    aim = models.CharField(max_length=200, default="Aim:")
    objectives = models.TextField(blank=True)
    activity = models.TextField()
    link = models.URLField(blank=True)
    public = models.BooleanField(default=not VISIBLE)  # will the plan be accessed by public (without login)
    assigned_users = models.ManyToManyField(Parent, blank=True)
    topics = models.ManyToManyField(Topic)  # which topic(s) does the lessonPlan belong to

    def __str__(self):
        return self.title
