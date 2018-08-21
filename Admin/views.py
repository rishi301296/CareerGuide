from django.shortcuts import render, HttpResponseRedirect, reverse
from SignUp.models import User_Authentication, User_Detail
from django.conf import settings
from .forms import RequestsForm
from django.forms.formsets import formset_factory
import itertools

def requestsView(request):
    if settings.LOGGED_IN != None and settings.LOGGED_IN.role == 'user':
        return HttpResponseRedirect(reverse('home'))
    
    if request.method == 'POST':
        ans, c = request.POST, 0
        for i in ans.keys():
            if i[:4] == 'form':
                if ans[i]:
                    item = (User_Authentication.objects.filter(email = qset[c]))[0]
                    User_Detail.objects.create(name = item.name, email = item.email, mobile = item.mobile, password = item.password, role = 'admin')
                    item.delete()
                c+=1
        return HttpResponseRedirect(reverse('adminRequests'))
    else:
        sets = User_Authentication.objects.all().values_list('email')
        qset = [str(u[0]) for u in sets]
        formset = formset_factory(RequestsForm, extra=len(qset))
    
    return render(request, 'admin.html', {
        'loggedin_student' : settings.LOGGED_IN,
        'formset' : dict(itertools.izip(qset, formset())),
        })