from django.db import models
from django.urls import reverse
# Create your models here.

class Person(models.Model):

    name = models.CharField(max_length=200)
    emailId = models.CharField(max_length=200)
    Contact = models.CharField(max_length=12)
    Image_1 = models.FileField()
    Image_2 = models.FileField()
    Image_3 = models.FileField()
    Image_4 = models.FileField()
    Image_5 = models.FileField()
    Train_status=models.CharField(max_length=1,default="n")
    person_id=models.CharField(max_length=500,default="")
    person_present_status= models.BooleanField(max_length=1,default=False)
    Present_number = models.IntegerField(default=0)
    Total_number = models.IntegerField(default=0)
    Fraud_number = models.IntegerField(default=0)
    flag = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse('camapp:details', kwargs={'pk':self.pk})


    def __str__(self):
        return self.name+ " , " +self.emailId



class TableAttendance(models.Model):
    name = models.CharField(max_length=200)
    personId = models.IntegerField(default = -1)
    time1 = models.TimeField(null=True)                             # to store the time when First Attendance confirmation mail was sent
    ts = models.TimeField(null=True)
    date = models.DateField(null=True)
    date_time = models.DateTimeField(null=True)


class Ipaddress(models.Model):
    ip = models.CharField(max_length=500)
    group_id = models.CharField(max_length=100, default="22")


class Fraud(models.Model):
    name = models.CharField(max_length=200)
    personId = models.IntegerField(default = -1)
    t1 = models.TimeField(null=True)
    t2 = models.TimeField(null=True)
    date = models.DateField(null=True)
    date_time = models.DateTimeField(null=True)


