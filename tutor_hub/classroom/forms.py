from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserCreationForm
        fields = ['username', 'first_name', 'last_name', 'email']
# Change the default email name from Email address to Email
        labels = {'email': 'Email'}
