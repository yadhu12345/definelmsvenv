from django.urls import path, include
from . import views

urlpatterns = [
path('', views.home,name="user_home"),
path('vxam/', views.vexam,name="vexam"),
path('allcourse/', views.allcourse,name="vcourse"),
path('about/', views.about,name="about"),
path('contact/', views.contact,name="contact"),
]