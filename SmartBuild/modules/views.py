from django.shortcuts     import render
from django.views.generic import ListView
from .models              import Module
from .forms               import ModuleFilterForm
# Create your views here.

class ModuleList(ListView):
	model               = Module
	context_object_name = 'modules'
	template_name       = 'modules/module_list.html'

	filter_form = None

	def dispatch(self, request):
		self.filter_form  = ModuleFilterForm(self.request.GET)
		return super(ModuleList, self).dispatch(request=request)

	def get_queryset(self):
		return super(ModuleList, self).get_queryset()
