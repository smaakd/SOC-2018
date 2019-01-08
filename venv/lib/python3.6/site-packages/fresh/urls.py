from django.conf.urls import patterns, url

from .views import fresh


urlpatterns = patterns('',
    url(r'^fresh/$', fresh, name='fresh'),
)

