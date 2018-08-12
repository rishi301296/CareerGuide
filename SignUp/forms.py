from django import forms
from .models import Student
from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class SignUpForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder' : 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Enter password'}))
    mobile = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(attrs={'placeholder' : 'Enter mobile No', 'type' : 'number'}))
    date_of_birth = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), choices=(('male', 'Male'),('female', 'Female')))
    school = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter high secondary school'}))
    stream = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter stream'}))
    entrance_exam = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder' : 'Enter exam name'}))
    rank = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder' : 'Enter rank', 'type' : 'number'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter address'}))
    father_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter father\'s name'}))
    father_mobile = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(attrs={'placeholder' : 'Enter father\'s mobile No', 'type' : 'number'}))

    def process(self):
        data = self.cleaned_data
        return data

    class Meta:
        model = Student
        fields = '__all__'