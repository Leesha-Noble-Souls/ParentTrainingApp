from django.contrib import admin

from .models import LessonPlan, Topic

admin.site.register(Topic)
admin.site.register(LessonPlan)
