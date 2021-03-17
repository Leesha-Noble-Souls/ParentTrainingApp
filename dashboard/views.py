from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from lessonPlans.models import LessonPlan

@login_required
def dashboard(request):
    current_user = request.user
    available_plans = []
    for plan in LessonPlan.objects.all():
        if current_user in plan.assigned_users.all():
            available_plans.append({"name": plan.title, "id" : plan.id})
    return render(request, "dashboard/index.html", {"available_plans" : available_plans})
