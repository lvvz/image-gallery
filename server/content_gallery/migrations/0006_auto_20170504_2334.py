# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 20:34
from __future__ import unicode_literals

from django.db import migrations
import content_gallery.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content_gallery', '0005_auto_20170320_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=content_gallery.fields.GalleryImageField(upload_to='gallery'),
        ),
    ]
