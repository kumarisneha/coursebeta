# Generated by Django 3.0.7 on 2020-06-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('course_type', models.CharField(choices=[('IT/Software', 'IT/software'), ('Engineering', 'engineering'), ('UPSE', 'upse'), ('SSC', 'ssc')], max_length=15)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='CourseType',
        ),
    ]
