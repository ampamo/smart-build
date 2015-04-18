# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=1, to='builds.Floor'),
            preserve_default=False,
        ),
    ]
