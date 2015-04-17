from django.contrib import admin
from .models        import IndicationType, Indication, ToModuleIndication, FromModuleIndication
# Register your models here.

class IndicationTypeAdmin(admin.ModelAdmin):
	list_display = ('id', )


class IndicationAdmin(admin.ModelAdmin):
	list_display = ('id', 'description', )


class ToModuleIndicationAdmin(admin.ModelAdmin):
	list_display = ('id', 'module', 'indication', 'order', )


class FromModuleIndicationAdmin(admin.ModelAdmin):
	list_display = ('id', 'module', 'indication', 'order', )


admin.site.register(IndicationType, IndicationTypeAdmin)
admin.site.register(Indication, IndicationAdmin)
admin.site.register(FromModuleIndication, FromModuleIndicationAdmin)
admin.site.register(ToModuleIndication, ToModuleIndicationAdmin)
