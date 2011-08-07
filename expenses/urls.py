from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import *
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$',householdsView, name='households'),
)
