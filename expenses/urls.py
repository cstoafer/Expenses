from django.conf.urls.defaults import patterns, url
from django.contrib import admin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from expenses.models import Person, Household, Transaction

admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^person/(?P<pk>\d+)$',DetailView.as_view(model=Person, context_object_name='person'), name='person'),
                       url(r'^household/(?P<pk>\d+)$',DetailView.as_view(model=Household, context_object_name='household'), name='household'),
                       url(r'^household/create/$',CreateView.as_view(model=Household, ), name='household_create'),
                       url(r'^transaction/create/$',CreateView.as_view(model=Transaction),name='transaction_create'),
)
