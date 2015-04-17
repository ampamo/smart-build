# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indication',
            name='without_stairs',
            field=models.BooleanField(default=True),
        ),
    ]
