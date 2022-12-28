from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def tutor(request):
    return render(request, 'tutor.html')


def student(request):
    return render(request, 'student.html')