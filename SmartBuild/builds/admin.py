# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models        import Build, Floor
# Register your models here.

class BuildAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', )

class FloorAdmin(admin.ModelAdmin):
	list_display = ('id', 'order', 'build', )

admin.site.register(Build, BuildAdmin)
admin.site.register(Floor, FloorAdmin)
