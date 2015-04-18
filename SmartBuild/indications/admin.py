from django.contrib import admin
from .models        import IndicationType, Indication, Route, RouteStep
# Register your models here.

class IndicationTypeAdmin(admin.ModelAdmin):
	list_display = ('id', )


class IndicationAdmin(admin.ModelAdmin):
	list_display = ('id', 'description', )


class RouteAdmin(admin.ModelAdmin):
	list_display = ('id', 'from_module', 'to_module', )


class RouteStepAdmin(admin.ModelAdmin):
	list_display = ('id', 'route', 'indication', 'order', )


admin.site.register(IndicationType, IndicationTypeAdmin)
admin.site.register(Indication, IndicationAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(RouteStep, RouteStepAdmin)
