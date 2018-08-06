# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def sign(request):
    return render(request, 'signup.html')