from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Tutor

# Create your views here.
def home(request):
    
    return render(request, 'home.html')


def tutor(request):
    if request.method == 'POST':
        name = request.POST[name]
        email = request.POST[email]
        subjectExpert = request.POST[sub]
        biodata = request.POST[bio]
        
        submit_btn = Submit(name=name, email=email, subjectExpert=sub, biodata=bio)
        new_tutor.save()
    return render(request, 'tutor.html')


def student(request):
    return render(request, 'student.html', {})