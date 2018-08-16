# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, reverse
from SignUp.models import Student 
from django.views.generic import TemplateView
from django.conf import settings

def homeView(request):
    if settings.LOGGED_IN == None:
        if request.session.has_key('email'):
            settings.LOGGED_IN = Student.objects.filter(email = request.session['email'])[0]
    return render(request, 'home.html', {'loggedin_student' : settings.LOGGED_IN})

def logoutView(request):
    print ('hdfhdvsnhvsddncvsdncvhnvwhbdwd')
    del request.session['email']
    settings.LOGGED_IN = None
    return HttpResponseRedirect(reverse('home'))