from django import forms
from SignUp.models import Student

class LoginForm(forms.ModelForm):
    email = forms.CharField(label = 'Email ', widget=forms.TextInput(attrs={'placeholder' : 'Enter email'}))
    password = forms.CharField(label = 'Password ', widget=forms.PasswordInput(attrs={'placeholder' : 'Enter password'}))

    class Meta:
        model = Student
        fields = ('email', 'password',)