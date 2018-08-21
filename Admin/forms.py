from django import forms
from SignUp.models import User_Authentication, User_Detail

class RequestsForm(forms.Form):
    option = forms.ChoiceField(
            label = '', 
            choices = [(True,'Accept'),(False,'Reject'),]
        )