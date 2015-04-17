# -*- encoding: utf-8 -*-
from django.shortcuts     import render
from django.views.generic import ListView
from .models              import Module
from .forms               import ModuleFilterForm

class ModuleList(ListView):
	model               = Module
	context_object_name = 'modules'
	template_name       = 'module_list.html'

	filter_form = None

	def dispatch(self, request):
		self.filter_form  = ModuleFilterForm(self.request.GET)
		return super(ModuleList, self).dispatch(request=request)

	def get_queryset(self):
		return super(ModuleList, self).get_queryset()

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(ModuleList, self).get_context_data(**kwargs)
		# Add filter_form
		context['module_filter_form'] = self.filter_form
		return context
