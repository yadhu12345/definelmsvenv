from django.urls import path, include
from . import views

urlpatterns = [
path('', views.home,name="index"),
path('vxam/', views.vexam,name="vexam"),
path('vcourse/<int:id>', views.vcourse,name="vcourse"),
path('vclass/<int:id>', views.vclass,name="vclass"),
path('about/', views.about,name="about"),
path('contact/', views.contact,name="contact"),
path('404/', views.error,name="404"),
path('loginu/', views.login,name="loginu"),
]