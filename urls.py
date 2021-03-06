from django.conf.urls.defaults import patterns, include, url
import settings
from django.contrib import admin
from expenses.forms import ProfileUpdateForm, MyRegistrationForm
from registration.views import register

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^expenses/', include('expenses.urls')),
	url(r'^accounts/register/$', register, 
		{'form_class': MyRegistrationForm}, 
		name='registration_register'),
    url(r'^accounts/', include('registration.urls')),
    url(r'^profiles/edit', 'profiles.views.edit_profile', {'form_class': ProfileUpdateForm}),
    url(r'^profiles/', include('profiles.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

urlpatterns+=patterns('',
                      url(r'^', include('frontend.urls',namespace='frontend',app_name='frontend')),
                      )
