# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20160902_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packs',
            name='number',
            field=models.CharField(max_length=10, verbose_name='Number of pack'),
        ),
    ]
