# -*- encoding: utf-8 -*-
from django.shortcuts     import render
from django.views.generic import ListView
from .models              import Module
from .forms               import ModuleFilterForm
from django.db.models     import Q
from indications.models   import RouteStep

class ModuleList(ListView):
	model               = Module
	context_object_name = 'modules'
	template_name       = 'module_list.html'

	filter_form = None

	from_module = None #módulo de inicio de ruta

	without_stairs_value = True

	def dispatch(self, request):
		self.filter_form = ModuleFilterForm(self.request.GET)
		self.from_module = Module.objects.get(name='Entrada') #De momento sólo Entrada
		return super(ModuleList, self).dispatch(request=request)

	def get_queryset(self):
		self.without_stairs_value = True
		if self.filter_form.has_changed():
			if 'reduced_mobility' in self.filter_form.data:
				self.without_stairs_value = not self.filter_form.data['reduced_mobility']

			route_ids = RouteStep.objects.filter(indication__without_stairs=self.without_stairs_value).distinct().values_list('route_id', flat=True)
			tag_filter            = Q(tag__name__icontains=self.filter_form.data['filter_value'])
			name_filter           = Q(name__icontains=self.filter_form.data['filter_value'])
			without_stairs_filter = Q(to_route__id__in=route_ids)

			return super(ModuleList, self).get_queryset().select_related().filter(name_filter | tag_filter, without_stairs_filter).distinct()

		route_ids = RouteStep.objects.filter(indication__without_stairs=self.without_stairs_value).distinct().values_list('route_id', flat=True)
		without_stairs_filter = Q(to_route__id__in=route_ids)
		return super(ModuleList, self).get_queryset().filter(without_stairs_filter).distinct()

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(ModuleList, self).get_context_data(**kwargs)
		# Add filter_form
		context['module_filter_form']   = self.filter_form
		# Add from_module
		context['from_module']          = self.from_module
		if self.without_stairs_value:
			context['without_stairs_value'] = 1
		else:
			context['without_stairs_value'] = 0
		return context
