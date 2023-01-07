from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
# Change the default email name from Email address to Email
        labels = {'email': 'Email'}
