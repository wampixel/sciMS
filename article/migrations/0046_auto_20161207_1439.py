# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0045_auto_20161207_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Categories'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]