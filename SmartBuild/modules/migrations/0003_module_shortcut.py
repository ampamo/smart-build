# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_module_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='shortcut',
            field=models.BooleanField(default=False),
        ),
    ]
