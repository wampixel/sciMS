# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0024_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('date_pub', models.DateField(verbose_name='date published')),
                ('categories', models.CharField(max_length=50)),
                ('abstract', models.CharField(max_length=1000)),
                ('keyword', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=100)),
                ('ref', models.CharField(max_length=1000)),
            ],
        ),
    ]
