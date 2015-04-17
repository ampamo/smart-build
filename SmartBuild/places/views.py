from django.shortcuts import render
from modules.forms    import ModuleFilterForm

# Create your views here.

def home(request):
	form        = ModuleFilterForm(request.POST or None)

	return render(request, 'index.html', {
		'form' : form
	})


