from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from camapp.models import Person,TableAttendance,Fraud, Ipaddress
import cognitive_face as CF
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import sys
import os
from script import main
import openpyxl as op



import glob
import threading
from script import live
from script import test1
import os
import shutil
import time


flag=0
global th

class IndexView(LoginRequiredMixin,generic.ListView):
    global flag
    template_name = 'camapp/index.html'
    context_object_name = 'flag'

    def get_queryset(self):
        return flag


class DetailView(LoginRequiredMixin,generic.DetailView):
    redirect_field_name = '/camapp/'
    model=Person
    template_name = 'camapp/details.html'

class Ipcreate(LoginRequiredMixin,generic.CreateView):
    redirect_field_name = '/camapp/'


    model = Ipaddress
    fields = ['ip']
    success_url = reverse_lazy('index')

class PersonCreate(LoginRequiredMixin,CreateView):
    redirect_field_name = '/camapp/'

    model = Person
    fields = ['name','emailId','Contact','Image_1','Image_2','Image_3','Image_4','Image_5']
    success_url = reverse_lazy('index')


class PersonUpdate(LoginRequiredMixin,UpdateView):
    redirect_field_name = '/camapp/'

    model=Person
    fields = ['name','emailId','Contact','Image_1','Image_2','Image_3','Image_4','Image_5']
    success_url = reverse_lazy('index')


class PersonDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = '/camapp/'

    model=Person
    success_url = reverse_lazy('index')




@login_required
def PersonTrain(request,pk):
    KEY = '332c42de6f6b4b399f55c0aee49c371e'                               # Replace with a valid Subscription Key here
    CF.Key.set(KEY)
    BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)
    group_id = "22"
    p=Person.objects.filter(id = pk)
    for person1 in p:
        x = CF.person.create(group_id, person1.name)
        person1.person_id = x['personId']
        CF.person.add_face(person1.Image_1, group_id, x['personId'])
        CF.person.add_face(person1.Image_2, group_id, x['personId'])
        CF.person.add_face(person1.Image_3, group_id, x['personId'])
        CF.person.add_face(person1.Image_4, group_id, x['personId'])
        CF.person.add_face(person1.Image_5, group_id, x['personId'])
        CF.person_group.train(group_id)
        person1.Train_status='y'
        person1.save()
    return redirect('index')


@login_required
def PresentList(request):
    #present_people=Person.objects.filter(person_present_status=True)
    present_people = TableAttendance.objects.all()
    template=loader.get_template('camapp/present_list.html')
    context={
        'present_people' : present_people,
    }
    return HttpResponse(template.render(context,request))

@login_required
def AttendanceList(request):
    all_people = Person.objects.all()
    template = loader.get_template('camapp/attendance_record.html')
    context = {
        'all_people': all_people,
    }
    return HttpResponse(template.render(context, request))

@login_required
def AttendanceDetails(request, pk):

    p = int(pk)
    person_details = Person.objects.filter(id = p)
    template = loader.get_template('camapp/attendance_details.html')
    context = {
        'person_details' : person_details,
    }
    return HttpResponse(template.render(context, request))


@login_required
def startAttendance(request, flag1):
    global th
    global flag
    flag = int(flag1)
    if (flag == 1):

        # p = Person.objects.filter(person_present_status=True)
        # for man in p:
        #     man.person_present_status = False
        #     man.save()


        p = Person.objects.all()
        for man in p:
            man.flag = 0
            man.Total_number = man.Total_number + 1
            man.person_present_status = False
            man.save()

        delete_previous_record = TableAttendance.objects.all()
        for dp in delete_previous_record:
            dp.delete()

        delete_previous_fraud = Fraud.objects.all()
        for f in delete_previous_fraud:
            f.delete()




        th = threading.Thread(target = main.start)
        th.flag=True
        th.start()

    if (flag == 0):
        th.flag=False
        th.join()

    # recordprint=TableAttendance.objects.all()
    # wb = op.load_workbook('/home/saketh/soc/report.xlsx')
    # ws = wb['Sheet']
    # for itr in recordprint:
    #     row = (itr.name,itr.personId,str(itr.date),str(itr.time1),str(itr.ts))
    #     ws.append(row)
    # wb.save('/home/saketh/soc/report.xlsx')
    # wb.close()
    return redirect('index')


@login_required
def fraudpeople(request):
    fraud_people = Fraud.objects.all()
    template=loader.get_template('camapp/fraud_list.html')
    context={
        'fraud_people' : fraud_people,
    }
    return HttpResponse(template.render(context,request))


@login_required
def ListAll(request):
    all_people = Person.objects.all()
    template=loader.get_template('camapp/list_all.html')
    context={
        'all_people':all_people,
    }
    return HttpResponse(template.render(context,request))


@login_required
def AboutUs(request):
    all_people = Person.objects.all()

    template=loader.get_template('camapp/about_us.html')

    context={
        'all_people':all_people,
    }
    return HttpResponse(template.render(context,request))

