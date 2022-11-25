from dataclasses import fields
from django import forms
from .models import *

class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    class Meta:
        model = login
        fields = ('username','password')
    
    
class courseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = ('course_name','description','amount','duration','exam','image','user')
        widgets = {
            'course_name': forms.TextInput(attrs={'class':'form-control', 'id':'courseid'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'amount'     : forms.NumberInput(attrs={'class':'form-control', 'id':'amountid'}),
            'duration'   : forms.TextInput(attrs={'class':'form-control', 'id':'durationid'}),
            'exam'       : forms.Select(attrs={'class':'form-control', 'id':'examid'}),
            'image'      : forms.FileInput(attrs={'class':'form-control', 'id':'imageid'}),
            'user'       : forms.Select(attrs={'class':'form-control', 'id':'userid'}),
        }

class subjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = ('subject_name','description','image','user')
        widgets = {
            'subject_name': forms.TextInput(attrs={'class':'form-control', 'id':'subjectid'},),
            'description' : forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'image'       : forms.FileInput(attrs={'class':'form-control', 'id':'imageid'}),
            'user'        : forms.Select(attrs={'class':'form-control', 'id':'userid'}),
        }

class examForm(forms.ModelForm):
    class Meta:
        model = exam
        fields = ('exam_name','description','remarks')
        widgets = {
            'exam_name':forms.TextInput(attrs={'class':'form-control', 'id':'examnameid'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'remarks':forms.TextInput(attrs={'class':'form-control', 'id':'remarksid'}),
        }

class topicForm(forms.ModelForm):
    class Meta:
        model  = topic
        fields = ('topic_name','description','subject','user')
        widgets = {
            'topic_name' : forms.TextInput(attrs={'class':'form-control', 'id':'topicid'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'subject'    :forms.Select(attrs={'class':'form-control', 'id':'subjectid'}),
            'user'       :forms.Select(attrs={'class':'form-control', 'id':'userid'}),
        }

class subtopicForm(forms.ModelForm):
    class Meta:
        model  = Subtopics
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'topic'    :forms.Select(attrs={'class':'form-control', 'id':'subjectid'}),
        }

class exammasterForm(forms.ModelForm):
    class Meta:
        model = exam_master
        fields ='__all__'
        widgets = {
            'name'       : forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'exam'       : forms.Select(attrs={'class':'form-control', 'id':'examid'}),
            'course'     : forms.Select(attrs={'class':'form-control', 'id':'courseid'}),
            'no_of_questions': forms.NumberInput(attrs={'class':'form-control', 'id':'noqid'}),
            'total_time' : forms.TimeInput(attrs={'class':'form-control', 'id':'ttimeid'}),
            'no_of_attempt': forms.NumberInput(attrs={'class':'form-control', 'id':'attemptid'}),
            'exam_start_date': forms.SelectDateWidget(attrs={'class':'form-control', 'id':'sdateid'}),
            'exam_end_date': forms.SelectDateWidget(attrs={'class':'form-control', 'id':'edateid'}),
            'exam_description': forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}),
            'is_draft'   : forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'userid'}),
            'user'       : forms.Select(attrs={'class':'form-control', 'id':'userid'}),
        }
     
class question_bankform(forms.ModelForm):
    class Meta:
        model = question_bank
        fields = "__all__"
        widgets = {
            'question':forms.TextInput(attrs={'class':'form-control', 'id':'questionid'}),
            'subject':forms.Select(attrs={'class':'form-control', 'id':'subjectid'}),
            'topic':forms.Select(attrs={'class':'form-control', 'id':'topicid'}),
            'subtopic':forms.Select(attrs={'class':'form-control', 'id':'subtopicid'}),
            'no_of_options':forms.NumberInput(attrs={'class':'form-control', 'id':'no_of_optionsid'}),
            'tags':forms.TextInput(attrs={'class':'form-control', 'id':'tagsid'}),
            'is_explanation':forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'is_explanationid'}),
            'is_image':forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'is_imageid'}),
            'explanation':forms.TextInput(attrs={'class':'form-control', 'id':'explanationid'}),
            'difficulty_level':forms.TextInput(attrs={'class':'form-control', 'id':'difficulty_levelid'}),
            'user':forms.Select(attrs={'class':'form-control', 'id':'userid'}),
            'status':forms.TextInput(attrs={'class':'form-control', 'id':'statusid'}),
            'remark':forms.TextInput(attrs={'class':'form-control', 'id':'remarkid'}),
            'is_reported':forms.NullBooleanSelect(attrs={'class':'form-control', 'id':'is_reportedid'}),
            'report_reason':forms.TextInput(attrs={'class':'form-control', 'id':'report_reasonid'}),
            'correct_answer':forms.TextInput(attrs={'class':'form-control', 'id':'correct_answerid'}),
            'option':forms.Textarea(attrs={'class':'form-control', 'id':'optionid','rows':3}),
        }

class optionsForm(forms.ModelForm):
    class Meta:
        model = question_bank_options
        fields = ('question','choice','identifier',)
        widgets = {
            'question': forms.Select(attrs={'class': 'form-control', 'id':'examnameid'}),
            'choice': forms.TextInput(attrs={'class': 'form-control','id':'descriptionid'}),
            'identifier': forms.TextInput(attrs={'class': 'form-control', 'id':'remarksid'}),
        }