from django.conf.urls import patterns, include, url
from django.contrib   import admin
from places.views     import home
from django.conf      import settings

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^places/', include('places.urls')),
]

if settings.DEBUG : # solo para desarrollo sirvo los archivos estaticos a traves del servidor de django
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root' : settings.MEDIA_ROOT
		})
	)
