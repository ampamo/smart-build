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
	from_module    = models.ManyToManyField(Module, through="FromModuleIndication", related_name='from_module')
	to_module      = models.ManyToManyField(Module, through="ToModuleIndication",   related_name='to_module')
	without_stairs = models.BooleanField(default=True)


	description = models.CharField(max_length=140)


class ToModuleIndication(models.Model):
	module     = models.ForeignKey(Module, on_delete=models.PROTECT, )
	indication = models.ForeignKey(Indication, on_delete=models.PROTECT)
	order      = models.PositiveIntegerField()


class FromModuleIndication(models.Model):
	module     = models.ForeignKey(Module, on_delete=models.PROTECT, )
	indication = models.ForeignKey(Indication, on_delete=models.PROTECT)
	order      = models.PositiveIntegerField()
