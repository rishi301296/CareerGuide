from django.shortcuts import render, HttpResponseRedirect, reverse
from SignUp.models import User_Authentication, User_Detail
from django.conf import settings
from .forms import RequestsForm, UpdateDbForm
from django.forms.formsets import formset_factory
import itertools
import csv
from io import StringIO
import codecs

def requestsView(request):
    if settings.LOGGED_IN != None:
        if settings.LOGGED_IN.role == 'user':
            return HttpResponseRedirect(reverse('home'))
    
    qset = [str(u[0]) for u in User_Authentication.objects.all().values_list('email')]
    formset = formset_factory(RequestsForm, extra=len(qset))
    if request.method == 'POST':
        ans, c = request.POST, 0
        for i in ans.keys():
            if i[:4] == 'form':
                if str(ans[i]) == 'True':
                    item = (User_Authentication.objects.filter(email = qset[c]))[0]
                    User_Detail.objects.create(name = item.name, email = item.email, mobile = item.mobile, password = item.password, role = 'admin')
                    item.delete()
                c+=1
    return render(request, 'admin.html', {
        'loggedin_student' : settings.LOGGED_IN,
        'formset' : dict(itertools.izip(qset, formset())),
        })

def updateDbView(request):
    print("start")
    if request.method == 'POST' and request.FILES:
        print(request.FILES)
        handle_uploaded_file(request.FILES["csv_file"])
        return HttpResponseRedirect(reverse('adminRequests'))   
    return render(request, 'updatedb.html', {'loggedin_student' : settings.LOGGED_IN})

def handle_uploaded_file(csvfile):
    dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
    csvfile.open()
    reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
    for row in reader:
        print(row)