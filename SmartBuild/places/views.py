# -*- encoding: utf-8 -*-
from django.shortcuts import render
from modules.forms    import ModuleFilterForm
from modules.models   import Module

# Create your views here.

def home(request):
	module_filter_form = ModuleFilterForm(request.POST or None)

	from_module = Module.objects.get(name='Entrada') #De momento sólo Entrada
	modules     = Module.objects.filter(shortcut=True).order_by('name')

	return render(request, 'index.html', {
		'module_filter_form' : module_filter_form,
		'from_module'        : from_module,
		'modules'            : modules
	})


