# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Build(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Floor(models.Model):
	build = models.ForeignKey(Build, on_delete=models.PROTECT)

	order = models.PositiveIntegerField()

	def __unicode__(self):
		return unicode(self.order) + u'-->' + self.build.name
