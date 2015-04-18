# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
        ('indications', '0002_indication_without_stairs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'indications', blank=True)),
                ('map_image', models.ImageField(upload_to=b'indications', blank=True)),
                ('from_module', models.ForeignKey(related_name='from_module', on_delete=django.db.models.deletion.PROTECT, to='modules.Module')),
                ('to_module', models.ForeignKey(related_name='to_module', on_delete=django.db.models.deletion.PROTECT, to='modules.Module')),
            ],
        ),
        migrations.CreateModel(
            name='RouteStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='frommoduleindication',
            name='indication',
        ),
        migrations.RemoveField(
            model_name='frommoduleindication',
            name='module',
        ),
        migrations.RemoveField(
            model_name='tomoduleindication',
            name='indication',
        ),
        migrations.RemoveField(
            model_name='tomoduleindication',
            name='module',
        ),
        migrations.RemoveField(
            model_name='indication',
            name='from_module',
        ),
        migrations.RemoveField(
            model_name='indication',
            name='to_module',
        ),
        migrations.DeleteModel(
            name='FromModuleIndication',
        ),
        migrations.DeleteModel(
            name='ToModuleIndication',
        ),
        migrations.AddField(
            model_name='routestep',
            name='indication',
            field=models.ForeignKey(to='indications.Indication', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='routestep',
            name='route',
            field=models.ForeignKey(to='indications.Route', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
