from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'lessonPlans'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:lessonPlan_id>/',  views.LessonPlanView.as_view(), name='detail'),
    path('topics/<int:topic_id>', views.topic_detail, name='topic-detail'),
]

urlpatterns += staticfiles_urlpatterns()
