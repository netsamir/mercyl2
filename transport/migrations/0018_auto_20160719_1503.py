# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0017_remove_bank_cost_various'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fix_cost',
            name='name',
            field=models.CharField(default='contadora', max_length=120),
        ),
    ]