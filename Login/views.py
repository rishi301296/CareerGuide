# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from .forms import LoginForm
from django.utils import timezone
from SignUp.models import Student
import hashlib as h
from django.conf import settings

template_login = 'login.html'

def loginView(request):
    if request.session.has_key('email'):
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            hashed_password = (h.md5(str(settings.MD5_SALT+form.cleaned_data['password']).encode())).hexdigest()
            if login(request, email, hashed_password, form):
                request.session['email'] = email
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginForm()
    return render(request, template_login, {'form' : form})

def login(request, Email, Password, form):
    data = Student.objects.filter(email = Email)
    if data[0].password == Password:
        return True
    return False