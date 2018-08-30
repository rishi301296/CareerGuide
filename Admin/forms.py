from django import forms
from SignUp.models import User_Authentication, User_Detail

class RequestsForm(forms.Form):
    option = forms.ChoiceField(
            label = '', 
            choices = [(True,'Accept'),(False,'Reject'),]
        )

class UpdateDbForm(forms.Form):
    course = forms.ChoiceField(
        label = "Course",
        choices = [('Engnieering','Engnieering'),('Law','Law'),('Management','Management'),('Medical','Medical'),],
        initial = 'Engnieering',
        )
    tableType = forms.ChoiceField(
        label = 'Table Type',
        choices = [('College_Basic_Detail','College_Basic_Detail'),('College_Placement_Detail','College_Placement_Detail'),],
        initial = 'College_Basic_Detail',)
    file = forms.FileField(
        label = 'Select file',
        help_text = 'Upload only .csv file'
        )