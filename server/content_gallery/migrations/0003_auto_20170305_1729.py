# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import content_gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('content_gallery', '0002_auto_20170305_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(upload_to='gallery/'),
        ),
    ]
