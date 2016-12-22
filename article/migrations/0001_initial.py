# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 15:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('add_date', models.DateField(default=datetime.date.today, verbose_name='add_date')),
                ('date_pub', models.DateField(verbose_name='date published')),
                ('abstract', models.CharField(max_length=1000)),
                ('keyword', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=100000)),
                ('ref', models.CharField(max_length=1000)),
                ('writer', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cat', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Categories'),
        ),
    ]
