# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='purchase',
            field=models.DecimalField(decimal_places=0, max_digits=7),
        ),
    ]