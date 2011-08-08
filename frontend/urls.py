from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$',login_required(TemplateView.as_view(template_name='home.html')), name='home'),
)
