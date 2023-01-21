from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_tutor = models.BooleanField('Is tutor', default=False)
    is_student = models.BooleanField('Is student/parent', default=False) 



class TutorReg(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor')
    name = models.CharField(max_length=255, default='default name')
    email = models.EmailField(max_length=255, default='default email')
    subject_experties = models.CharField(max_length=100, default='default subject')
    bio = models.TextField(default='')

class StudentReg(models.Model):
  #  user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='student')
    name = models.CharField(max_length=100, default='default name')
    email = models.EmailField(default='default email')
    subject_required = models.CharField(max_length=100, default='default subject')
    contact_number = models.CharField(max_length=13, default='0000000000')
    
    
#class Student(models.Model):
  #  user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional fields specific to students

#class Tutor(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional fields specific to tutors
 


