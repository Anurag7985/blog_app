from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Tutor
from django.views.decorators.csrf import requires_csrf_token


# Create your views here.
def home(request):
    
    return render(request, 'home.html')


@requires_csrf_token
def tutor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject_expert = request.POST.get('subjectExpert')
        biodata = request.POST.get('bio')
        submit_obj = Tutor(name=name, email=email, subject_experties=subject_expert, bio=biodata)
        submit_obj.save()
  
    return render(request, 'tutor.html')



def student(request):
    return render(request, 'student.html', {})