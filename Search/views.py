# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def searchView(request):
    return render(request, 'search.html')
