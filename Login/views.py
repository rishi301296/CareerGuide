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
        print('yooooooooooooooooooooooooooooo')
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print('maaa kasam neend a rha h')
        if form.is_valid():
            print('aaoouuuuu')
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('chlo ayaaaaaaaaaa')
            if login(request, email, password, form):
                request.session['email'] = email
                print('haaaaaaaaaaaanjiiii')
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginForm()
    return render(request, template_login, {'form' : form})

def login(request, Email, Password, form):
    print ('login checkkkkkkkkkkkkkkkkk')
    data = Student.objects.filter(email = Email)
    print(data)
    if data[0].password == Password:
        return True
    return False