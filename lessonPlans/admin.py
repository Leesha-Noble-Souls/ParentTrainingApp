from django.contrib import admin

from .models import LessonPlan, Topic, LessonFeedback,OnlineTraining,ShortCourses,Webinar,FreeSession
admin.site.site_header = 'Vyom Self Help Foundation'
admin.site.register(Topic)
admin.site.register(LessonPlan)
admin.site.register(LessonFeedback)
admin.site.register(Webinar)
admin.site.register(OnlineTraining)
admin.site.register(ShortCourses)
admin.site.register(FreeSession)
