from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Tutor
from jobs.models import Resgistration
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@requires_csrf_token
def register(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm()
    return render(request, 'tsignup.html',{'form':fm})

        
        
    



def home(request):
    
    return render(request, 'home.html')



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