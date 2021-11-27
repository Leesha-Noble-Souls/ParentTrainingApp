"""parentTraining URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles import views
from django.contrib import admin
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('contact', views.contact, name='contact'),
    path('lessonPlans/', include('lessonPlans.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('autism/', views.autism,name='autism'),
    path('webinar/', views.webinar,name='webinar'),
    path('work_areas/', views.work_areas,name='work_areas'),
    path('assessment/', views.assessment,name='assessment'),
    path('onlineTraining/', views.onlineTraining,name='onlineTraining'),
    path('shortCourse/', views.shortCourse,name='shortCourse'),
    path('terms-conditions/', views.termsconditions, name='termsconditions'),
    path('privacy-policy/', views.privacypolicy, name='privacypolicy')

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path(
        'accounts/login', 
        LoginView.as_view(redirect_authenticated_user=True), 
        name='login'
        ),
]
