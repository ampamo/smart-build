# -*- encoding: utf-8 -*-
from django.shortcuts     import get_object_or_404
from django.views.generic import ListView
from .models              import Route, RouteStep
from modules.models       import Module
from modules.forms        import ModuleFilterForm

# Create your views here.

class RouteStepList(ListView):
	model               = RouteStep
	context_object_name = 'routesteps'
	template_name       = 'routestep_list.html'

	module      = None
	filter_form = None

	def dispatch(self, request, from_module_pk, to_module_pk, from_slug, to_slug):
		self.route       = get_object_or_404(Route, from_module=from_module_pk, to_module=to_module_pk)
		self.filter_form = ModuleFilterForm(self.request.GET)
		return super(RouteStepList, self).dispatch(request=request)

	def get_queryset(self):
		return self.route.routestep_set.all().order_by('order')

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(RouteStepList, self).get_context_data(**kwargs)
		# Add filter_form
		context['module_filter_form'] = self.filter_form
		# Add route
		context['route'] = self.route
		return context

