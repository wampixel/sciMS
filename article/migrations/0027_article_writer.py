# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0026_auto_20161129_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]
