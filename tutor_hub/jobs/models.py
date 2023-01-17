from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=20)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    


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
 
    

class Job(models.Model):
    student = models.ForeignKey(StudentReg, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)

class Application(models.Model):
    tutor = models.ForeignKey(TutorReg, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cover_letter = models.TextField()

