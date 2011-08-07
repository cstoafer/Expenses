from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib import admin
from frontend.views import PersonView, HouseholdView

admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$',login_required(TemplateView.as_view(template_name='home.html')), name='home'),
                       url(r'^person/(?P<pk>\d+)$',PersonView.as_view(), name='person'),
                       url(r'^household/(?P<pk>\d+)$',HouseholdView.as_view(), name='household'),
)
