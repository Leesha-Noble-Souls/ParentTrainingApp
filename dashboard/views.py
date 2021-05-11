from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from lessonPlans.models import LessonPlan

@login_required
def dashboard(request):
    current_user = request.user
    available_plans = {}

    for plan in LessonPlan.objects.all():
        if current_user in plan.assigned_users.all():
            for topic in plan.topics.all() :
                available_plans.setdefault(topic, []).append({"id" : plan.id, "title": plan.title, "aim":plan.aim})
                # available_plans.setdefault(topic, []).append({"id" : plan.id, "title": plan.title, "aim":plan.aim, "topics" : plan.topics.all()})
        
    return render(request, "dashboard/index.html", {"available_plans" : available_plans})
