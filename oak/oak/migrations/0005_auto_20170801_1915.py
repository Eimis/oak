# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 19:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oak', '0004_auto_20170801_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamelog',
            name='from_column',
        ),
        migrations.RemoveField(
            model_name='gamelog',
            name='from_row',
        ),
    ]
