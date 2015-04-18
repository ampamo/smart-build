# -*- encoding: utf-8 -*-
from django.db      import models
from modules.models import Module

# Create your models here.

class IndicationType(models.Model):
	TEXT  = 1
	SOUND = 2

	Types = (
        (TEXT,  'Texto'),
        (SOUND, 'Sonido'),
    )

	def get_default_name(self):
		for t in IndicationType.Types:
			if t[0] == self.id:
				return t[1]
		return None

	id = models.IntegerField(primary_key=True, choices=Types)

	def __unicode__(self):
		return self.get_default_name()


class Indication(models.Model):
	kind           = models.ForeignKey(IndicationType, on_delete=models.PROTECT)
	without_stairs = models.BooleanField(default=True)

	description    = models.TextField()

	def __unicode__(self):
		return self.description


class Route(models.Model):
	from_module = models.ForeignKey(Module, on_delete=models.PROTECT, related_name='from_route')
	to_module   = models.ForeignKey(Module, on_delete=models.PROTECT, related_name='to_route')
	image       = models.ImageField(blank=True, upload_to='indications')
	map_image   = models.ImageField(blank=True, upload_to='indications')

	def __unicode__(self):
		return self.from_module.name + u'-->' + self.to_module.name


class RouteStep(models.Model):
	route      = models.ForeignKey(Route, on_delete=models.PROTECT)
	indication = models.ForeignKey(Indication, on_delete=models.PROTECT)
	order      = models.PositiveIntegerField()

	def __unicode__(self):
		return unicode(self.order) + u'. ' + unicode(self.route)

