

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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeedBackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = form.save()
            post.user = request.user;
            post.save();
            context['form']= form
            print("Hello", FeedBack.objects.all())
        else:
            print("Invalid")
        return render(request, 'lessonPlans/feedback_form.html', {'form': form})
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    # form = FeedBackForm(request.POST or None, request.FILES or None)
    # print(form)
    # # check if form data is valid
    # if form.is_valid():
    #     # save the form data to model
    #     print(form)
    #     form.save()
  
    # context['form']= form
    # # return HttpResponse("Oye oye")

    # return render(request, 'lessonPlans/feedback_form.html', {'form': form})


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