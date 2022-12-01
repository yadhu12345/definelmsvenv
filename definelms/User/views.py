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

def vcourse(request,id):
    exm = course.objects.filter(exam=id)
    context = {
        'xm' : exm
    }
    return render(request, 'User_UI/allcourse.html',context)

def tutorial(request):
    return render(request, 'User_UI/tutorials.html')

def about(request):
    return render(request, 'User_UI/about.html')

def contact(request):
    return render(request, 'User_UI/contact.html')

def error(request):
    return render(request, 'User_UI/404.html')

#{% static 'userui/img/course-1.jpg' %}
def login(request):
    return render(request, 'User_UI/login.html')