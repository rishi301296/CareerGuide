from django import forms
from .models import Current_User

class LoginForm(forms.ModelForm):
    email = forms.CharField(label = 'Email ')
    password = forms.CharField(label = 'Password ')

    class Meta:
        model = Current_User
        fields = ('email', 'password',)