# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160517_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomBrokerPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_cif_inf', models.DecimalField(decimal_places=2, max_digits=7)),
                ('valor_cif_sup', models.DecimalField(decimal_places=2, max_digits=7)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUruguay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=120)),
                ('recargo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('imudani', models.DecimalField(decimal_places=2, max_digits=7)),
                ('tsa', models.DecimalField(decimal_places=2, max_digits=7)),
                ('extraordinario', models.DecimalField(decimal_places=2, max_digits=7)),
                ('guia', models.DecimalField(decimal_places=2, max_digits=7)),
                ('tasa', models.DecimalField(decimal_places=2, max_digits=7)),
                ('anticipo_irae', models.DecimalField(decimal_places=2, max_digits=7)),
                ('anticipo_imesi', models.DecimalField(decimal_places=2, max_digits=7)),
                ('puerto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=7)),
                ('anticipo_iva', models.DecimalField(decimal_places=2, max_digits=7)),
                ('gastos_y_otros', models.DecimalField(decimal_places=2, max_digits=7)),
                ('flete_local', models.DecimalField(decimal_places=2, max_digits=7)),
                ('playa_de_contenedores', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraordinarioPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_cif_inf', models.DecimalField(decimal_places=2, max_digits=7)),
                ('valor_cif_sup', models.DecimalField(decimal_places=2, max_digits=7)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('purchase_price', models.DecimalField(decimal_places=0, max_digits=7)),
                ('sale_price', models.DecimalField(decimal_places=0, max_digits=7)),
                ('sold_price', models.DecimalField(decimal_places=0, max_digits=7)),
                ('weight', models.DecimalField(decimal_places=0, max_digits=7)),
                ('length', models.DecimalField(decimal_places=0, max_digits=7)),
                ('width', models.DecimalField(decimal_places=0, max_digits=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ton_inf', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ton_sup', models.DecimalField(decimal_places=2, max_digits=7)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TasaServicioAduana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_cif_inf', models.DecimalField(decimal_places=2, max_digits=7)),
                ('valor_cif_sup', models.DecimalField(decimal_places=2, max_digits=7)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaxCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=120)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
