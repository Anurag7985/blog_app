from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserCreationForm
        fields = ['field1', 'field2', 'field3']
# Change the default email name from Email address to Email
        labels = {'email': 'Email'}
