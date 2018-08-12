# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from .forms import LoginForm
from django.utils import timezone
from SignUp.models import Student
from Home.views import homeView

template_login = 'login.html'

def loginView(request):
    if request.session.has_key('email'):
        email = request.session['email']
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if login(request, email, password, form):
                request.session['email'] = email
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, template_login, {'form' : form})

def login(request, email, password, form):
    if Student.objects.all() == None:
        return False
    data = Student.objects.all()
    for data_obj in data:
        if data_obj.email == email and data_obj.password == password:
            return True
    return False