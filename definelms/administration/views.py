from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from lmsmainapp.models import *
from lmsmainapp.forms import *


#login
def admin_login(request):
	msg=''
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		userlogin=login.objects.filter(username=username,password=password,role=0).count()
		if userlogin > 0:
			userlogin=login.objects.filter(username=username,password=password,role=0).first()
			request.session['username']=userlogin.username
			return redirect('home')
		else:
			msg='Invalid!!'
            
	form=AdminLoginForm
	return render(request, 'administration/login.html',{'forms':form,'msg':msg})
 
def admin_logout(request):
    logout(request)
    return redirect('login')

def home_page(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        total_course   = course.objects.count()
        uname=request.session['username']
        total_subject  = subject.objects.count()
        total_exam     = exam.objects.count()
        total_question = question_bank.objects.count()
        context={
        'course'  :total_course,
        'subject' :total_subject,
        'exam'    :total_exam,
        'question':total_question,
        'uuname':uname
        }
        return render(request, 'home.html', context)
        
def home(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        form = DepartmentForm()
        dsn = Department.objects.all()
        context = {'form':form, 'dsn':dsn}
        return render(request, 'administration/home.html', context)


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            did = request.POST.get('dsnid')
            designation = request.POST['designation']
            print('student id',did)

            if(did == ''):
                d = Department(designation=designation)
            else:
                d = Department(id=did, designation=designation)
            d.save()

            dsn = Department.objects.values()
            student_data = list(dsn)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        d = Department.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        print('Student ID',id)
        desgn = Department.objects.get(pk=id)
        student_data = {'id':desgn.id, 'designation':desgn.designation}
        return JsonResponse(student_data)


#add course
def addcourse(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            
            form = courseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = course.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'course/course1.html',context)
        else:
            form = courseForm()
        designation=course.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'course/course1.html', context)


@csrf_exempt
def delete_data_course(request):
    if request.method == 'POST':
        id = request.POST.get('cid')
        d = course.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    



#add subject

def addsubject(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = subjectForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = subject.objects.all()
                us = login.objects.all
                context = {'form': form, 'st': designation,'uu':us}
                return render(request, 'subject/subject.html',context)
        else:
            form = subjectForm()
        designation=subject.objects.all()
        us = login.objects.all
        context = {'form': form, 'st': designation,'uu':us}
        return render(request, 'subject/subject.html', context)

@csrf_exempt
def delete_data_subject(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        d = subject.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0}) 


#add exam


def home_exam(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        form = examForm()
        exm = exam.objects.all()
        context = {'form':form, 'exm':exm}
        return render(request, 'exam/addexam.html', context)


@csrf_exempt
def save_data_exam(request):
    if request.method == 'POST':
        form = examForm(request.POST)
        if form.is_valid():
            eid = request.POST.get('exmid')
            exam_name = request.POST['exam_name']
            description = request.POST['description']
            remarks = request.POST['remarks']
            if(eid == ''):
                s = exam(exam_name=exam_name, description=description, remarks=remarks)
            else:
                s = exam(id=eid, exam_name=exam_name, description=description, remarks=remarks)
            s.save()

            exm = exam.objects.values()
            exam_data = list(exm)
            return JsonResponse({'status':'Data Saved', 'exam_data':exam_data})
        else:
            return JsonResponse({'status':'Not Saved'})    


@csrf_exempt
def delete_data_exam(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        s = exam.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data_exam(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        examo = exam.objects.get(pk=id)
        exam_data = {'id':examo.id, 'exam_name':examo.exam_name, 'description':examo.description, 'remarks':examo.remarks}
        return JsonResponse(exam_data)


#add topic


def addtopic(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = topicForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = topic.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'topic/addtopic.html',context)
        else:
            form = topicForm()
        designation=topic.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'topic/addtopic.html', context)


@csrf_exempt
def delete_data_topic(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        s  = topic.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data_topic(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        examo = topic.objects.get(pk=id)
        exam_data = {'id':examo.id, 'topic_name':examo.topic_name, 'description':examo.description, 'subject':examo.subject, 'user':examo.user}
        return JsonResponse(exam_data)



#add subtopic

def addsubtopic(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = subtopicForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = Subtopics.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'subtopic/addsubtopic.html',context)
        else:
            form = subtopicForm()
        designation=Subtopics.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'subtopic/addsubtopic.html', context)


@csrf_exempt
def delete_data_subtopic(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        s  = Subtopics.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data_subtopic(request):
    if request.method == 'POST':
        id = request.POST.get('eid')
        examo = Subtopics.objects.get(pk=id)
        exam_data = {'id':examo.id, 'topic_name':examo.topic_name, 'description':examo.description, 'subject':examo.subject, 'user':examo.user}
        return JsonResponse(exam_data)

#add question

def add_question(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = question_bankform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = question_bank.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'questionbank/questionbank.html',context)
                
        else:
            form = question_bankform()
        designation = question_bank.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'questionbank/questionbank.html', context)  

@csrf_exempt
def delete_data_question(request):
    if request.method == 'POST':
        id = request.POST.get('qid')
        s = question_bank.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

#add options

def addoptions(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = optionsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                option = question_bank_options.objects.all()
                context = {'form': form, 'opn': option}
                return render(request, 'qsoptions/topic.html',context)
                
        else:
            form = optionsForm()
        option = question_bank_options.objects.all()
        context = {'form': form, 'opn': option}
        return render(request, 'qsoptions/topic.html',context)





@csrf_exempt
def delete_data_addoptions(request):
    if request.method == 'POST':
        id = request.POST.get('oid')
        d = question_bank_options.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0}) 


@csrf_exempt
def edit_data_addoptions(request):
    if request.method == 'POST':
        id = request.POST.get('oid')
        #print('Exam ID',id)
        examo = topic.objects.get(pk=id)
        exam_data = {'id':examo.id, 'exam_name':examo.exam_name,'description':examo.description,'remarks':examo.remarks}
        return JsonResponse(exam_data)

#add exam master

def addexmaster(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = exammasterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                designation = exam_master.objects.all()
                context = {'form': form, 'st': designation}
                return render(request, 'exam_master/exammaster.html',context)
        else:
            form = exammasterForm()
        designation=exam_master.objects.all()
        context = {'form': form, 'st': designation}
        return render(request, 'exam_master/exammaster.html', context)


@csrf_exempt
def delete_data_exmaster(request):
    if request.method == 'POST':
        id = request.POST.get('emid')
        s  = exam_master.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data_exmaster(request):
    if request.method == 'POST':
        id = request.POST.get('emid')
        examo = exam_master.objects.get(pk=id)
        exam_data = {'id':examo.id, 'topic_name':examo.topic_name, 'description':examo.description, 'subject':examo.subject, 'user':examo.user}
        return JsonResponse(exam_data)