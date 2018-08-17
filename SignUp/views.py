# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Student
from .forms import SignUpForm
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
            data = form.save(commit = False)
            email = form.cleaned_data['email']
            hashed_password = (h.md5(str(settings.MD5_SALT+form.cleaned_data['password']).encode())).hexdigest()
            data.password = hashed_password
            print (hashed_password)
            data.save()
            request.session['email'] = email
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignUpForm()
    return render(request, template_signup, {'form' : form})
'''
def formView(request):
   if request.session.has_key('email'):
      username = request.session['email']
      return redirect(template_home)
   else:
      return redirect(template_signup)
'''