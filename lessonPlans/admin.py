from django.contrib import admin

from .models import LessonPlan, Topic, LessonFeedback

admin.site.register(Topic)
admin.site.register(LessonPlan)
admin.site.register(LessonFeedback)
