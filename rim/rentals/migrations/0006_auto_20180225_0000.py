# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-25 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_rental_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='brand',
            field=models.CharField(default='Madshus', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gear',
            name='gear_type',
            field=models.CharField(default='Boots', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gear',
            name='size',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]