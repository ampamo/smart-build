from django.db import models

# Create your models here.

class Build(models.Model):
	name = models.CharField(max_length=50)


class Floor(models.Model):
	build = models.ForeignKey(Build, on_delete=models.PROTECT)

	order = models.PositiveIntegerField()
