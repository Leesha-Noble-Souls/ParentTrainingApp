

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .models import FeedBack, LessonPlan, Topic
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FeedBackForm

def get_name(request):
    
    context ={}
    if request.method == 'GET':
        return HttpResponse("Yayy")
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            try:
                post = form.save(commit = False);
                
                post.name = request.user.username + "_" + str(form.cleaned_data['lessons']);
                context['form']= post
                post.save();
            except Exception as e:
                return render(request, 'lessonPlans/error_form.html')
        return render(request, 'lessonPlans/feedback_form.html', {'form': form})
            #


def index(request):
    return HttpResponse("Hello, world")

def detail(request, lessonPlan_id):
    try:
        lessonPlan = LessonPlan.objects.get(pk = lessonPlan_id)
        link = str(LessonPlan.objects.get(pk = lessonPlan_id).link)
        YT1 = "youtube.com"
        YT2 = "youtu.be"
        index = link.find(YT1)
        if index == -1:
            index = link.find(YT2)
            YT = YT2
        else:
            YT = YT1
        print(index)
        link = link[:index] + YT1 + "/embed" + link[index+len(YT):]
        print(link)
    except:
        raise Http404("Lesson plan does not exist")
    if lessonPlan.public or (request.user in lessonPlan.assigned_users.all()):
        return render(request, 'lessonPlans/detail.html', {'lessonPlan' : lessonPlan, 'link' : link})
    return redirect('/accounts/login')

def topic_detail(request, topic_id):
    try:
        topic = Topic.objects.get(pk = topic_id)
        description = topic.description
    except ObjectDoesNotExist:
        raise Http404("Topic does not exist")
    return render(request, 'lessonPlans/topic_detail.html', {'topic' : topic})