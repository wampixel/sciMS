# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='article.categories'),
        ),
    ]