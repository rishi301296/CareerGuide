from django import forms
from .models import Student

class SignUpForm(forms.ModelForm):

    name = forms.CharField(label = 'Name', widget=forms.TextInput(attrs={'placeholder' : 'Enter name', 'class' : 'formfield'}))
    email = forms.EmailField(label = 'Email', widget=forms.TextInput(attrs={'placeholder' : 'Enter email', 'class' : 'formfield'}))
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'placeholder' : 'Enter password', 'class' : 'formfield'}))
    mobile = forms.CharField(label = 'Mob No.', max_length=10, min_length=10, widget=forms.TextInput(attrs={'placeholder' : 'Enter mobile No', 'class' : 'formfield'}))
    date_of_birth = forms.DateField(label = 'Date Of Birth', widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD', 'class':'formfield'}))
    gender = forms.ChoiceField(label = 'Gender', widget=forms.Select(attrs={'class' : 'genderfield'}), choices=[('male','Male'),('female','Female'),('Don\'t want to disclose','Don\'t want to disclose')])
    school = forms.CharField(label = 'School', widget=forms.TextInput(attrs={'placeholder' : 'Enter high secondary school', 'class' : 'formfield'}))
    stream = forms.CharField(label = 'Stream', widget=forms.TextInput(attrs={'placeholder' : 'Enter stream', 'class' : 'formfield'}))
    entrance_exam = forms.CharField(label = 'Entrance Exam', required=False, widget=forms.TextInput(attrs={'placeholder' : 'Enter exam name', 'class' : 'formfield'}))
    rank = forms.CharField(label = 'Exam Rank', required=False, widget=forms.TextInput(attrs={'placeholder' : 'Enter rank', 'class' : 'formfield'}))
    address = forms.CharField(label = 'Address', widget=forms.TextInput(attrs={'placeholder' : 'Enter address', 'class' : 'formfield'}))
    father_name = forms.CharField(label = 'Father\'s Name', widget=forms.TextInput(attrs={'placeholder' : 'Enter father\'s name', 'class' : 'formfield'}))
    father_mobile = forms.CharField(label = 'Father\'s Mob No.', max_length=10, min_length=10, widget=forms.TextInput(attrs={'placeholder' : 'Enter father\'s mobile No', 'class' : 'formfield'}))

    class Meta:
        model = Student
        fields = '__all__'