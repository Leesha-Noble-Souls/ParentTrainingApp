from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]

urlpatterns += staticfiles_urlpatterns()
