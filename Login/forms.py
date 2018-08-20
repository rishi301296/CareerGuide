from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label = 'Email ', widget=forms.TextInput(attrs={'placeholder' : 'Enter email'}))
    password = forms.CharField(label = 'Password ', widget=forms.PasswordInput(attrs={'placeholder' : 'Enter password'}))