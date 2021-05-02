# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20170618_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True),
        ),
    ]
