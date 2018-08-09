# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import SignUpForm

class SignUp:
    template_signup = 'signup.html'

    def get_signup(self, request):
        form = SignUpForm()
        return render(request, self.template_signup, {'form' : form})

    def post_signup(self, request):
        form = request.POST
        return render(request, self.template_signup, {'text' : form.get("name")})