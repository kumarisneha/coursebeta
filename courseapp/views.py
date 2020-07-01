
from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm, CourseCreationForm
from django.core.mail import send_mail, EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context
from django.conf import settings 
   
   
def index(request):
    return render(request, 'user/index.html',{'title':'index'})


# def home_view(request): 
#     context = {} 
#     context['form'] = GeeksForm() 
#     return render( request, "home.html", context) 

    # if request.method == "POST":
    #     form = CreationForm(request.POST)
    #     if form.is_valid():
    #         create = form.save()
    #         return redirect('post_detail', pk=create.pk)
    # else:
    #     form = PostForm()
    # return render(request, 'blog/post_edit.html', {'form': form})
def create_course(request):
    context = {} 
    context['form'] = CourseCreationForm()
    if request.method == "POST": 
        form = CourseCreationForm(request.POST)
        if form.is_valid():
            course_title = request.POST['course_title'] 
            course_type = request.POST['course_type'] 
            description = request.POST['description']
            form.save()
            print(course_title, course_type, description) 
            return render(request, 'submit_course.html')
    return render(request, 'create_course.html',context)

########################################################################
########### register here #####################################

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
            except Exception as e:
                print(e)
                print("error in sending mail")
            ##################################################################
            form.save()
            username = form.cleaned_data.get('username')
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