# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-03 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20160902_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('group', models.CharField(max_length=10, verbose_name='Number of pack')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='packs',
        ),
    ]
