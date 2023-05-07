from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'pages/home.html', {'projects': projects})

def about(request):
    return render(request, 'pages/about.html')





# Create your views here.
