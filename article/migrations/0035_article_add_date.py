# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 14:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0034_remove_article_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='add_date',
            field=models.DateField(default=datetime.date.today, verbose_name='add_date'),
        ),
    ]
