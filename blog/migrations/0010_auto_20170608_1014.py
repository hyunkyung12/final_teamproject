# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-08 01:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170530_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Tags',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='TagModel',
        ),
    ]
