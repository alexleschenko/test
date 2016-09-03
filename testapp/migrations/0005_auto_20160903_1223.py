# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-03 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20160903_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('question', models.TextField(max_length=100, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0432\u043e\u043f\u0440\u043e\u0441\u0430')),
                ('a1', models.TextField(max_length=50, verbose_name='\u041f\u0435\u0440\u0432\u044b\u0439 \u043e\u0442\u0432\u0435\u0442')),
                ('a2', models.TextField(max_length=50, verbose_name='\u0412\u0442\u043e\u0440\u043e\u0439 \u043e\u0442\u0432\u0435\u0442')),
                ('a3', models.TextField(max_length=50, verbose_name='\u0422\u0440\u0435\u0442\u0438\u0439 \u043e\u0442\u0432\u0435\u0442')),
                ('a4', models.TextField(blank=True, max_length=50, verbose_name='\u0427\u0435\u0442\u0432\u0435\u0440\u0442\u044b\u0439 \u043e\u0442\u0432\u0435\u0442')),
                ('a5', models.TextField(blank=True, max_length=50, verbose_name='\u041f\u044f\u0442\u044b\u0439 \u043e\u0442\u0432\u0435\u0442')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='group',
            name='group',
            field=models.CharField(max_length=10, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u0440\u0443\u043f\u043f\u044b \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432'),
        ),
        migrations.AddField(
            model_name='question',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Group'),
        ),
    ]