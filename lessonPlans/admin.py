from django.contrib import admin

from .models import FeedBack, LessonPlan, Topic

admin.site.register(Topic)
admin.site.register(LessonPlan)
admin.site.register(FeedBack)