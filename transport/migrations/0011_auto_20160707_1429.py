# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0010_honorarios_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='width',
            field=models.DecimalField(decimal_places=2, default=2.29, max_digits=10),
        ),
    ]
