from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from jobs.models import Tutor
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@requires_csrf_token
def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html',{'form':fm})

def login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/tutor/')
    else:
        fm = AuthenticationForm()
    return render(request,'login.html',{'form':fm})

        
        
    



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