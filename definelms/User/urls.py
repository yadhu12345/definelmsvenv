from django.urls import path, include
from . import views

urlpatterns = [
path('', views.home,name="index"),
path('vxam/', views.vexam,name="vexam"),
path('vcourse/', views.vcourse,name="vcourse"),
path('about/', views.about,name="about"),
path('contact/', views.contact,name="contact"),
]