from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import LessonPlan

def index(request):
    return HttpResponse("Hello, world")

def detail(request, lessonPlan_id):
    try:
        print(lessonPlan_id)
        lessonPlan = LessonPlan.objects.get(pk = lessonPlan_id)
    except:
        raise Http404("Lesson plan does not exist")
    return render(request, 'lessonPlans/detail.html', {'lessonPlan' : lessonPlan})
