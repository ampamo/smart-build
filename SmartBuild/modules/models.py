# -*- encoding: utf-8 -*-
from django.db                      import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers       import reverse
from builds.models                  import Floor

# Create your models here.

class Module(models.Model):
	floor = models.ForeignKey(Floor, on_delete=models.PROTECT)
	name  = models.CharField(max_length=50)

	def get_absolute_indication_list_url(self, from_module):
		return reverse('indication_list', kwargs={ 'from_module_pk' : from_module.pk, 'from_slug' : slugify(from_module.name), 'to_module_pk': self.pk, 'to_slug' : slugify(self.name) })

	def __unicode__(self):
		return self.name

class Tag(models.Model):
	modules = models.ManyToManyField(Module)
	name    = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
