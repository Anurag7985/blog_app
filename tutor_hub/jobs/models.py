from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#User.objects.all().delete()



class Tutor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject_experties = models.CharField(max_length=100)
    bio = models.TextField(default='')

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject_required = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=13, primary_key=True)
    
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    # additional fields specific to students

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    # additional fields specific to tutors
 
    

class Job(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)

class Application(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cover_letter = models.TextField()

