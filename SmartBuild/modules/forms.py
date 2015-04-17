# -*- encoding: utf-8 -*-
from django import forms

class ModuleFilterForm(forms.Form):
	filter_value   = forms.CharField(label='Busca un sitio', required=False)
	without_stairs = forms.BooleanField(label='Movilidad Reducida', required=False)
