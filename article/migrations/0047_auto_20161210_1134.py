# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0046_auto_20161207_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='summary',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='articles',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Categories'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.CharField(max_length=100000),
        ),
    ]