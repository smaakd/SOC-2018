from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name="details"),
    url(r'person/add/$',views.PersonCreate.as_view(), name='person-add'),
    # /camapp/person/2/
    url(r'person/(?P<pk>[0-9]+)/$', views.PersonUpdate.as_view(), name='person-update'),
    # /camapp/person/2/delete
    url(r'person/(?P<pk>[0-9]+)/delete/$', views.PersonDelete.as_view(), name='person-delete'),
    url(r'person/(?P<pk>[0-9]+)/train/$', views.PersonTrain, name='person-train'),
    url(r'person/present/$',views.PresentList, name='present-people'),
    url(r'person/attendance/(?P<flag1>[0-9])/$',views.startAttendance,name='attendance'),

    url(r'person/fraud/$',views.fraudpeople , name ='fraud-people'),
    url(r'person/all/$',views.ListAll, name='list-all'),
    url(r'person/attendancedetails/$', views.AttendanceList, name='attendance_list'),
    url(r'person/attendancedetails/(?P<pk>[0-9]+)/$', views.AttendanceDetails, name='attendance_details'),
    url(r'id/$', views.Ipcreate.as_view(), name='ip'),
    # url(r'person/present/ajax/$', views.ViewAjax, name='ajax_of_present'),
    url(r'about/$',views.AboutUs, name='about_us'),

	
]
