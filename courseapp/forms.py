from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import CourseCreate

COURSE_TYPE_CHOICE= [
    ('IT/Software', 'IT/software'),
    ('Engineering', 'engineering'),
    ('UPSE', 'upse'),
    ('SSC', 'ssc'),
    ]

class CourseCreationForm(forms.ModelForm):
    course_type= forms.CharField(widget=forms.Select(choices=COURSE_TYPE_CHOICE))

    class Meta:
        model = CourseCreate
        fields = '__all__'

class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField() 
    first_name = forms.CharField(max_length = 20) 
    last_name = forms.CharField(max_length = 20) 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] 
