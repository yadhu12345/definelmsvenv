from django.urls import path, include
from . import views


urlpatterns = [

    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('home/', views.home_page,name="home"),

    path('', views.home, name='home1'),
    path('save/', views.save_data, name='save'),
    path('delete/', views.delete_data, name='delete'),
    path('edit/', views.edit_data, name='edit'),

    # path('course', views.home_course, name='addc'),
    path('addcourse/', views.addcourse,name="addcourse"),
    path('deletecrs/', views.delete_data_course, name='deletec'),

    #subject setting

    path('addsubject/', views.addsubject,name="addsubject"),
    path('deletesub/', views.delete_data_subject, name='deletes'),

    #Exam Settings

    path('ex/', views.home_exam, name='homeex'),
    path('saveex/', views.save_data_exam, name='saveex'),
    path('deleteex/', views.delete_data_exam, name='deleteex'),
    path('editex/', views.edit_data_exam, name='editex'),

    #Topic Settings

    path('tp/', views.addtopic, name='hometp'),
    #path('savetp/', views.save_data_topic, name='savetp'),
    path('deletetp/', views.delete_data_topic, name='deletetp'),
    path('edittp/', views.edit_data_topic, name='edittp'),

    #Subtopic settings

    path('st/', views.addsubtopic, name='homest'),
    path('deletest/', views.delete_data_subtopic, name='deletest'),
    path('editst/', views.edit_data_subtopic, name='editst'),

    #question bank
    
    path('questionbankadd/', views.add_question, name='qbadd'),
    # path('savet/', views.save_data_topic, name='savetp'),
    path('questionbankdelete/', views.delete_data_question, name='deleteqb'),
    # path('editt/', views.edit_data_topic, name='edittp'),
    
    #Options

    path('op', views.addoptions, name='op'),
    path('deleteop/', views.delete_data_addoptions, name='deleteop'),
    path('editop/', views.edit_data_addoptions, name='editop'),

    #Exam master

    path('em/', views.addexmaster, name='homeem'),
    path('deleteem/', views.delete_data_exmaster, name='deleteem'),
    path('editst/', views.edit_data_exmaster, name='editst'),

]