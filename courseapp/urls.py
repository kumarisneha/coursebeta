from django.urls import path, include 
from django.conf import settings 
from courseapp import views
from django.conf.urls.static import static 
  
urlpatterns = [ 
         path('', views.index, name ='index'), 
         path('create_course', views.create_course, name ='create_course'), 
         path('add_topic/<int:title_id>/', views.add_topic, name ='add_topic'),
         path('^link$', views.link, name='link'),
] 
