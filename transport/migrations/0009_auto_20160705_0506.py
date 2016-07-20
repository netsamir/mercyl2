# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0008_auto_20160705_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puerto',
            name='multiplicator',
            field=models.DecimalField(decimal_places=2, default=13, max_digits=6),
        ),
        migrations.AlterField(
            model_name='puerto',
            name='ratio_low',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='puerto',
            name='ratio_up',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=10),
        ),
    ]