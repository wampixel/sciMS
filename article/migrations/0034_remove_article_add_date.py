# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0033_auto_20161205_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='add_date',
        ),
    ]