# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_auto_20160705_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='aduana',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
        ),
        migrations.AddField(
            model_name='honorarios',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
        ),
        migrations.AddField(
            model_name='puerto',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
        ),
    ]
