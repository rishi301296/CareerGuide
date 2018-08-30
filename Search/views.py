# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Admin.models import College_Basic_Detail, College_Placement_Detail
from django.shortcuts import render
from django.views.generic import TemplateView

class SearchView(TemplateView):
    college_list = []
    def get(self, request):
        return render(request, 'search.html', {'college_list' : self.college_list})
    
    def post(self, request):
        if self.college_list == []:
            location = request.get('location')
            stream = request.get('stream')
            budget = request.get('budget')
            print(location, stream, budget)
            #self.college_list = 
        else:
            location = request.get('location')
            stream = request.get('stream')
            budget = request.get('budget')
            print(location, stream, budget)
        return render(request, 'search.html', {'college_list' : self.college_list})