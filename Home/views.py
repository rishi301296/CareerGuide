# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from django.conf import settings
from SignUp.models import User_Detail

def homeView(request):
    if settings.LOGGED_IN != None:
        if settings.LOGGED_IN.role == 'admin':
            return HttpResponseRedirect(reverse('adminRequests'))
    return render(request, 'home.html', {'loggedin_student' : settings.LOGGED_IN})

def logoutView(request):
    del request.session['email']
    settings.LOGGED_IN = None
    return HttpResponseRedirect(reverse('home'))