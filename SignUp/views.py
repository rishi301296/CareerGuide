# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Student
from .forms import SignUpForm
import Home

class SignUp(TemplateView):
    template_signup = 'signup.html'
    template_home = 'Home\templates\home.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_signup, {'form' : form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_home, {'form' : form})