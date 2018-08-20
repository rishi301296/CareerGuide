# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import User_Detail, User_Authentication
from .forms import SignUpForm,AuthForm
import Home
import hashlib as h
from django.conf import settings

template_signup = 'signup.html'
template_home = 'home.html'

def signupview(request):
    if request.session.has_key('email'):
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            if role == 'User':
                data = form.save(commit = False)
                email = form.cleaned_data['email']
                hashed_password = (h.md5(str(settings.MD5_SALT+form.cleaned_data['password']).encode())).hexdigest()
                data.password = hashed_password
                print (hashed_password)
                data.save()
                request.session['email'] = email
            else:
                form = AuthForm(request.POST)
                form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignUpForm()
    return render(request, template_signup, {'form' : form})
