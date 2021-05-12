from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from lessonPlans.models import LessonPlan

@login_required
def dashboard(request):
    current_user = request.user
    topic_to_plans = {}

    for plan in LessonPlan.objects.all():
        if current_user in plan.assigned_users.all():
            for topic in plan.topics.all() :
                topic_to_plans.setdefault(topic, []).append({"id" : plan.id, "title": plan.title, "aim":plan.aim})
                # topic_to_plans.setdefault(topic, []).append({"id" : plan.id, "title": plan.title, "aim":plan.aim, "topics" : plan.topics.all()})
        
    return render(request, "dashboard/index.html", {"topic_to_plans" : topic_to_plans})
