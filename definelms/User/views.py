from django.shortcuts import render
from lmsmainapp.models import *

def home(request):
    exm = exam.objects.all()
    context = {
        'xm':exm
    }
    return render(request, 'User_UI/index.html',context)

def vexam(request):
    exm = exam.objects.all()
    context = {
        'xm' : exm
    }
    return render(request, 'User_UI/viewallexam.html',context)

def allcourse(request):
    return render(request, 'User_UI/allcourse.html')

def about(request):
    return render(request, 'User_UI/about.html')

def contact(request):
    return render(request, 'User_UI/contact.html')