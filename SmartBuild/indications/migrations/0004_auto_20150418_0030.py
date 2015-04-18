# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indications', '0003_auto_20150418_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indication',
            name='description',
            field=models.TextField(),
        ),
    ]
