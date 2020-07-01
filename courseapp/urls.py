from django.urls import path, include 
from django.conf import settings 
from courseapp import views
from django.conf.urls.static import static 
  
urlpatterns = [ 
         path('', views.index, name ='index'), 
         path('create_course', views.create_course, name ='create_course'), 
] 

