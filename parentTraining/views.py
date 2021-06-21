from django.shortcuts import render
from django.http import HttpResponse, Http404

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
