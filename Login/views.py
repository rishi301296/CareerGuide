# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import LoginForm
from .models import Current_User
from django.utils import timezone

class loginView(TemplateView):
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form' : form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['email']
            form.save()
        args = {'form' : form, 'text' : text}
        return render(request, 'login.html', args)