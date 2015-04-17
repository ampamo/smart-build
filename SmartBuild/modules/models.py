from django.db import models

# Create your models here.

class Module(models.Model):
	name = models.CharField(max_length=50)

class Tag(models.Model):
	modules = models.ManyToManyField(Module)

	name    = models.CharField(max_length=50)
