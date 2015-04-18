# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_module_shortcut'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='image',
            field=models.ImageField(upload_to=b'modules', blank=True),
        ),
    ]
