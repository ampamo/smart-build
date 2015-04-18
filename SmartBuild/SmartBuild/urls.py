from django.conf.urls import patterns, include, url
from django.contrib   import admin
from places.views     import home
from django.conf      import settings
#from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^admin/',       include(admin.site.urls)),
    url(r'^places/',      include('places.urls')),
    url(r'^modules/',     include('modules.urls')),
    url(r'^indications/', include('indications.urls')),
]

#urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG : # solo para desarrollo sirvo los archivos estaticos a traves del servidor de django
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root' : settings.MEDIA_ROOT
		})
	)

#from django.contrib.staticfiles import views

#if settings.DEBUG:
#    urlpatterns += [
#        url(r'^static/(?P<path>.*)$', views.serve),
#    ]
