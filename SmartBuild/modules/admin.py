from django.contrib import admin
from .models        import Module, Tag
# Register your models here.

class ModuleAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', )

class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', )

admin.site.register(Module, ModuleAdmin)
admin.site.register(Tag, TagAdmin)
