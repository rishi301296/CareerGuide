# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from .forms import LoginForm
from django.utils import timezone
from SignUp.models import User_Detail
import hashlib as h
from django.conf import settings

template_login = 'login.html'

def loginView(request):
    if request.session.has_key('email'):
        email = request.session['email']
        role = (User_Detail.objects.filter(email = email)[0]).role
        if role == 'admin':
            return HttpResponseRedirect(reverse('adminRequests'))
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            hashed_password = (h.md5(str(settings.MD5_SALT+form.cleaned_data['password']).encode())).hexdigest()
            if login(request, email, hashed_password):
                request.session['email'] = email
                settings.LOGGED_IN = User_Detail.objects.filter(email = email)[0]
                if settings.LOGGED_IN.role == 'admin':
                    return HttpResponseRedirect(reverse('adminRequests'))
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginForm()
    return render(request, template_login, {'form' : form})

def login(request, Email, Password):
    data = User_Detail.objects.filter(email = Email)
    try:
        if data[0].password == Password:
            return True
    except IndexError:
        return False
    return False