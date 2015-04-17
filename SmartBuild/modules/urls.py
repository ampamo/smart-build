from django.conf.urls import url, include
from .views           import ModuleList

urlpatterns = [
	url(r'^$', ModuleList.as_view(), name='module_list'),
]
