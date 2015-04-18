# -*- encoding: utf-8 -*-
from django import forms

class ModuleFilterForm(forms.Form):
	filter_value     = forms.CharField(label='Busca un sitio', required=False)
	reduced_mobility = forms.BooleanField(label='Movilidad Reducida', required=False)
