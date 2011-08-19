from django.conf.urls.defaults import patterns, include, url
from chihuo.views import main_view
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chihuo.views.home', name='home'),
    # url(r'^chihuo/', include('chihuo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^$', 'chihuo.views.main_view'),
	url(r'^category/(\d+)/$', 'chihuo.views.category_view'),
	
	#url(r'^rsvp/$', 'chihuo.rsvp.views.index'),
	url(r'^rsvp/create/$', 'chihuo.rsvp.views.create_event_step1'),
	url(r'^rsvp/create/create-event-step-1/$', 'chihuo.rsvp.views.create_event_step1'),
	url(r'^rsvp/create/create-event-step-2/$', 'chihuo.rsvp.views.create_event_step2'),
	url(r'^rsvp/create/create-event-step-3/$', 'chihuo.rsvp.views.create_event_step3'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )