# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0008_packagerental_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='note',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rental',
            name='note',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
