from django.shortcuts import render, HttpResponseRedirect, reverse
from SignUp.models import User_Authentication, User_Detail
from .models import College_Basic_Detail, College_Placement_Detail
from django.conf import settings
from .forms import RequestsForm, UpdateDbForm
from django.forms.formsets import formset_factory
import itertools
import csv
from io import StringIO
import codecs, threading

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
                elif str(ans[i]) == 'Delete':
                    item = (User_Authentication.objects.filter(email = qset[c]))[0]
                    item.delete()
                c+=1
    return render(request, 'admin.html', {
        'loggedin_student' : settings.LOGGED_IN,
        'formset' : dict(itertools.izip(qset, formset())),
        })

def updateDbView(request):
    print("startttttttttttt ",settings.LOGGED_IN)
    if request.method == 'POST':
        form = UpdateDbForm(request.POST,request.FILES)
        print("Formmmmmmmmmmmmmmmmmmm---",form,"  --- End")
        if form.is_valid():
            print('yooooooooooooooooooooooo---- End')
            course = form.cleaned_data['course']
            tableType = form.cleaned_data['tableType']
            file_content = form.cleaned_data['file']
            print("Dataaaaaaaaaaaaaaaaaa---",file_content,"---End")
            handle_uploaded_file(file_content, course, tableType)
        return HttpResponseRedirect(reverse('updatedb'))
    else:
        form = UpdateDbForm()
    return render(request, 'updatedb.html', {'loggedin_student' : settings.LOGGED_IN, 'form' : form})

def handle_uploaded_file(csvfile, course, table):
    dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
    csvfile.open()
    reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
    c=False
    if table == 'College_Basic_Detail':
        for row in reader:
            if len(row)==4 and c :
                try:
                    item = College_Basic_Detail.objects.get(collegeId = row[0])
                    item.courses += '$'+course
                except:
                    College_Basic_Detail.objects.create(
                        collegeId = row[0],
                        name = row[1],
                        city = row[2],
                        state = row[3],
                        courses = course)
            c=True
    elif table == 'College_Placement_Detail':
        for row in reader:
            if len(row)==5 and c:
                College_Placement_Detail.objects.create(
                    college = College_Basic_Detail.objects.filter(collegeId=row[0])[0],
                    totalStudents = int(row[1]),
                    placedStudents = int(row[2]),
                    averageSalary = int(row[4]),
                    course = course)
            c=True