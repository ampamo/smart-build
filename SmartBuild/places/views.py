# -*- encoding: utf-8 -*-
from django.shortcuts import render
from modules.forms    import ModuleFilterForm

# Create your views here.

def home(request):
	module_filter_form = ModuleFilterForm(request.POST or None)

	return render(request, 'index.html', {
		'module_filter_form' : module_filter_form
	})


