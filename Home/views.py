# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from SignUp.models import Student 
from django.views.generic import TemplateView

class homeView(TemplateView):
    loggedin_student = None 

    def get(self, request):
        if self.request.session.has_key('email') and self.loggedin_student == None:
            self.loggedin_student = Student.objects.filter(email=request.session['email'])[0]
        return render(request, 'home.html', {'loggedin_student' : self.loggedin_student})