from django.contrib import admin
from .models import Person,Fraud,TableAttendance,Ipaddress
# Register your models here.

admin.site.register(Person)
admin.site.register(Fraud)
admin.site.register(TableAttendance)
admin.site.register(Ipaddress)