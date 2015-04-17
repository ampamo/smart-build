# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FromModuleIndication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Indication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=140)),
                ('from_module', models.ManyToManyField(related_name='from_module', through='indications.FromModuleIndication', to='modules.Module')),
            ],
        ),
        migrations.CreateModel(
            name='IndicationType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, choices=[(1, b'Texto'), (2, b'Sonido')])),
            ],
        ),
        migrations.CreateModel(
            name='ToModuleIndication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField()),
                ('indication', models.ForeignKey(to='indications.Indication', on_delete=django.db.models.deletion.PROTECT)),
                ('module', models.ForeignKey(to='modules.Module', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.AddField(
            model_name='indication',
            name='kind',
            field=models.ForeignKey(to='indications.IndicationType', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='indication',
            name='to_module',
            field=models.ManyToManyField(related_name='to_module', through='indications.ToModuleIndication', to='modules.Module'),
        ),
        migrations.AddField(
            model_name='frommoduleindication',
            name='indication',
            field=models.ForeignKey(to='indications.Indication', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='frommoduleindication',
            name='module',
            field=models.ForeignKey(to='modules.Module', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
