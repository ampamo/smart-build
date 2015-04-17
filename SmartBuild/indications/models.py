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

	id = models.IntegerField(primary_key=True, choices=Types)

class Indication(models.Model):
	type        = models.ForeignKey(IndicationType, on_delete=models.PROTECT)
	from_module = models.ForeignKey(Module, on_delete=models.PROTECT)
	to_module   = models.ForeignKey(Module, on_delete=models.PROTECT)


	description = models.CharField(max_length=140)
	order       = models.PositiveIntegerField()
