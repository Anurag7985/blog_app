from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Tutor
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth import authenticate, login


# Create your views here.

def tutor_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(tutor_signup)
    else:
        form = SignUpForm()
    return render(request, 't_signup.html', {'form': form})
        
        
    



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