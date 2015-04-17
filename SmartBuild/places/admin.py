from django.contrib import admin
from .models        import Place
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', )


admin.site.register(Place, PlaceAdmin)
