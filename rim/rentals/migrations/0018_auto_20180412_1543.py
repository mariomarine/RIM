# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-12 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0017_auto_20180409_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateTimeField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateTimeField(verbose_name='end date'),
        ),
    ]
