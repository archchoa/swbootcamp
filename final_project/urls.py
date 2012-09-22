from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
	('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    url(r'^posts/', 'core.views.list_posts'),
    url(r'^admin/', include(admin.site.urls)),
)
