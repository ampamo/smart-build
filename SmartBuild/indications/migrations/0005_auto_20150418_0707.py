# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indications', '0004_auto_20150418_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='from_module',
            field=models.ForeignKey(related_name='from_route', on_delete=django.db.models.deletion.PROTECT, to='modules.Module'),
        ),
        migrations.AlterField(
            model_name='route',
            name='to_module',
            field=models.ForeignKey(related_name='to_route', on_delete=django.db.models.deletion.PROTECT, to='modules.Module'),
        ),
    ]
