# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Student
from .forms import SignUpForm
import Home

template_signup = 'signup.html'
template_home = 'home.html'

def signupview(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            request.session['email'] = email
            return render(request, template_home, {'form' : form})
        else:
            form = SignUpForm()
    return redirect(template_signup)
'''
def formView(request):
   if request.session.has_key('email'):
      username = request.session['email']
      return redirect(template_home)
   else:
      return redirect(template_signup)
'''