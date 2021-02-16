from django.shortcuts import render
from django.http import HttpResponse, Http404

def home(request):
    return render(request, 'parentTraining/home.html')
