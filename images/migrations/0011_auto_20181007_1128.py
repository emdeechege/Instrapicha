# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-07 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_auto_20181006_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='image',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
