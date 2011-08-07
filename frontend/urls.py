from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import homeView
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$',homeView, name='home'),
)
