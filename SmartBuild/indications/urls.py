# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from .views           import RouteStepList

urlpatterns = [
	url(r'^from/(?P<from_module_pk>\d+)-(?:(?P<from_slug>[\w-]+))/to/(?P<to_module_pk>\d+)-(?:(?P<to_slug>[\w-]+))?/$', RouteStepList.as_view(), name='routestep_list'),
]
