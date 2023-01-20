from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_tutor', 'is_student']
# Change the default email name from Email address to Email
        labels = {'email': 'Email'}
