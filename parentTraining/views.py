from django.shortcuts import render
from lessonPlans.models import Topic

def home(request):
    return render(request, 'parentTraining/home.html')

def about(request):
    return render(request, 'parentTraining/about.html')

def team(request):
    return render(request, 'parentTraining/team.html')

def testimonials(request):
    return render(request, 'parentTraining/testimonials.html')

def contact(request):
    return render(request, 'parentTraining/contact.html')

def autism(request):
    return render(request, 'parentTraining/about-autism.html')

def webinar(request):
    return render(request, 'parentTraining/webinar.html')

def assessment(request):
    return render(request, 'parentTraining/assessment.html')

def onlineTraining(request):
    return render(request, 'parentTraining/onlineTraining.html')

def shortCourse(request):
    return render(request, 'parentTraining/shortCourse.html')

def work_areas(request):
    return render(request, "parentTraining/work_areas.html", {"topics" : Topic.objects.all()})