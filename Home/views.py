# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def homeView(request):
    return render(request, 'home.html')
    
