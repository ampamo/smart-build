from django.db import models

# Create your models here.

class Place(models.Model):

	name = models.CharField(max_length=50)


class Tag(models.Model):
	places = models.ManyToManyField(Place, on_delete=models.ON_PROTECT)

	name = models.CharField(max_length=50)
