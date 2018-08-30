from django import forms
from .models import User_Detail, User_Authentication

class SignUpForm(forms.ModelForm):
    name = forms.CharField(
        label = 'Name',
        widget = forms.TextInput(
            attrs={'placeholder' : 'Enter name', 'class' : 'formfield'}
        )
    )
    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(
            attrs={'placeholder' : 'Enter email', 'class' : 'formfield'}
        )
    )
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {'placeholder' : 'Enter password', 'class' : 'formfield'}
        )
    )
    mobile = forms.CharField(
        label = 'Mob No.',
        max_length = 10,
        min_length = 10,
        widget = forms.TextInput(
            attrs={'placeholder' : 'Enter mobile No', 'class' : 'formfield'}
        )
    )
    role = forms.ChoiceField(
        label = 'Role',
        widget = forms.Select(
            attrs = {'class' : 'formfield'}),
            choices = [('admin','Admin'),('user','User'),]
    )

    class Meta:
        model = User_Detail
        fields = ['name', 'email', 'password', 'mobile', 'role']

class UpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(label = 'Date Of Birth', widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD', 'class':'formfield'}))
    gender = forms.ChoiceField(label = 'Gender', widget=forms.Select(attrs={'class' : 'genderfield'}), choices=[('male','Male'),('female','Female'),('Don\'t want to disclose','Don\'t want to disclose')])
    school = forms.CharField(label = 'School', widget=forms.TextInput(attrs={'placeholder' : 'Enter high secondary school', 'class' : 'formfield'}))
    city = forms.CharField(label = 'City', widget=forms.TextInput(attrs={'placeholder' : 'Enter your city', 'class' : 'formfield'}))
    state = forms.CharField(label = 'State', widget=forms.TextInput(attrs={'placeholder' : 'Enter your state', 'class' : 'formfield'}))
    father_name = forms.CharField(label = 'Father\'s Name', widget=forms.TextInput(attrs={'placeholder' : 'Enter father\'s name', 'class' : 'formfield'}))
    father_mobile = forms.CharField(label = 'Father\'s Mob No.', max_length=10, min_length=10, widget=forms.TextInput(attrs={'placeholder' : 'Enter father\'s mobile No', 'class' : 'formfield'}))

    class Meta:
        model = User_Detail
        fields = ['date_of_birth', 'gender', 'school', 'city', 'state', 'father_name', 'father_mobile']

class AuthForm(forms.ModelForm):
    name = forms.CharField(label = 'Name', widget=forms.TextInput(attrs={'placeholder' : 'Enter name', 'class' : 'formfield'}))
    email = forms.EmailField(label = 'Email', widget=forms.TextInput(attrs={'placeholder' : 'Enter email', 'class' : 'formfield'}))
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'placeholder' : 'Enter password', 'class' : 'formfield'}))
    mobile = forms.CharField(label = 'Mob No.', max_length=10, min_length=10, widget=forms.TextInput(attrs={'placeholder' : 'Enter mobile No', 'class' : 'formfield'}))
    role = forms.ChoiceField(label = 'Role', widget=forms.Select(attrs={'class' : 'genderfield'}), choices=[('admin','Admin'),('user','User'),])

    class Meta:
        model = User_Authentication
        fields = ['name', 'email', 'password', 'mobile', 'role']