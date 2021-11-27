from django.db import models
from dashboard.models import Parent
from django.contrib.auth import get_user_model
from django.conf import settings

User = settings.AUTH_USER_MODEL
VISIBLE = True


class Topic(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField()
    parent_topic = models.ForeignKey('self', null=True, blank=True, related_name='parentTopic',
                                     on_delete=models.CASCADE)

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

    def get_title(self):
        return self.title


class LessonFeedback(models.Model):
    username = models.ForeignKey(Parent, blank=True, null=True, on_delete=models.PROTECT, db_constraint=False)
    lesson = models.ForeignKey(LessonPlan, blank=True, null=True, on_delete=models.PROTECT, db_constraint=False)
    status = models.CharField(max_length=100)
    prompts = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    feedback = models.TextField(blank=True)

    def __str__(self):
        if self.lesson is not None:
            return self.username.get_username() + ": " + self.lesson.get_title()
        else:
            return self.username.get_username()


class Webinar(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    date = models.CharField(max_length=200, default="")
    details = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class OnlineTraining(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    details = models.TextField(blank=True)
    highlight = models.TextField(blank=True)
    register_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='static/images/',blank=True)

    def __str__(self):
        return self.title

    def delete(self):
        self.image.delete()
        super(ShortCourses, self).delete()


class ShortCourses(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    details = models.TextField(blank=True)
    highlight = models.TextField(blank=True)
    register_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='static/images/',blank=True)

    def __str__(self):
        return self.title

    def delete(self):
        self.image.delete()
        super(ShortCourses, self).delete()

class FreeSession(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    details = models.TextField(blank=True)
    highlight = models.TextField(blank=True)
    link_text = models.TextField(blank=True)
    register_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='static/images/',blank=True)

    def __str__(self):
        return self.title

    def delete(self):
        self.image.delete()
        super(FreeSession, self).delete()
