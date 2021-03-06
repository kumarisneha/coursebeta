from django.db import models

# Create your models here.
COURSE_TYPE_CHOICE= [
    ('IT/Software', 'IT/software'),
    ('Engineering', 'engineering'),
    ('UPSE', 'upse'),
    ('SSC', 'ssc'),
    ]

class CourseCreate(models.Model):
    course_title = models.CharField(max_length=50, unique = True)
    course_type = models.CharField(max_length=15, choices=COURSE_TYPE_CHOICE)
    description = models.TextField(max_length=300)

class SyllabusAddition(models.Model):
    topic = models.CharField(max_length=50)
    link = models.CharField(max_length=250)
    title = models.ForeignKey(CourseCreate, blank=True, null=True, on_delete=models.SET_NULL)
