from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Role


class SignUpForm(UserCreationForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all())
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
# Change the default email name from Email address to Email
        labels = {'email': 'Email'}
