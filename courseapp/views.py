
from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm, CourseCreationForm, SyllabusAdditionForm
from .models import SyllabusAddition, CourseCreate
from django.core.mail import send_mail, EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context
from django.conf import settings 
from django.http import HttpResponseRedirect
   
def index(request):
    return render(request, 'user/index.html',{'title':'index'})

def link(request):
    return render(request, 'user/index.html')

def create_course(request):
    context = {} 
    context['form'] = CourseCreationForm()
    if request.method == "POST":
        print("inside-------------------")
        form = CourseCreationForm(request.POST)
        print(form.is_valid)
        print("form---------", form)
        course_title = request.POST['course_title']
        course_type = request.POST['course_type']
        description = request.POST['description']
        if form.is_valid():
            form.save()
            obj = CourseCreate.objects.get(course_title = course_title)
            context['course_title'] = course_title
            context['course_type'] = course_type
            context['description'] = description
            context['obj'] = obj
            print(course_title, course_type, description, request.POST)
            print(context)
            # return redirect('add_topic', id=obj.id)
            # return HttpResponseRedirect(reverse('add_topic', kwargs={'id': obj.id}))
            return HttpResponseRedirect('/add_topic/%d' % obj.id)
        else:

            obj = CourseCreate.objects.get(course_title = course_title)
            print(form.errors['course_title'].as_data())
            print ("objjjjjjjjjjj", obj)
            # print(form.item.errors.as_text())
            for t in form.errors['course_title'].as_data():
                context['text'] = t
                print(type(t))

            # [u'This field is required.']
            # if obj.course_title == course_title:
            #     t = "Course title already exists. Please give another title"
            #     context['text'] = t
            #     print(context)
            #     print(form.errors)
            return render(request,'create_course.html', context)

    print("outside-------------------")
    return render(request, 'create_course.html',context)

def add_topic(request, title_id):
    print("------------",title_id)
    context = {}
    context['form'] = SyllabusAdditionForm()
    context['title_id'] = title_id
    context['add_syllabus'] = SyllabusAddition.objects.filter(title_id=title_id)
    if request.method == "POST":
        form = SyllabusAdditionForm(request.POST)
        if form.is_valid():
            course_topic = request.POST['topic']
            course_link = request.POST['link']
            instance = form.save(commit=False)
            print(request.session)
            print(form)
            instance.title_id = title_id
            instance.save()
            print("instance----------",instance)
            print(course_topic, course_link)
            context['add_syllabus'] = SyllabusAddition.objects.filter(title_id=title_id)
            # obj = CourseCreate.objects.get(course_title = course_title)
            print("coooooooooo",context)
            return render(request, 'submit_course.html', context)
    return render(request, 'submit_course.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            #########################mail####################################
            htmly = get_template('user/email.html')
            print("----------------", htmly)
            d = { 'username': username }
            subject, from_email, to = 'welcome to Coursebeta world', settings.EMAIL_HOST_USER, email
            html_content = htmly.render(d)
            # message = f'Hi {username}, thank you for registering in Coursebeta.'

            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                # send_mail( subject, html_content, from_email, [to] )
                msg.send()
                print("Mail sent successfully")
            except Exception as e:
                print(e)
                print("error in sending mail")
            ##################################################################
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form,'title':'register here'})

###################################################################################
################login forms###################################################

def Login(request):
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form,'title':'log in'})