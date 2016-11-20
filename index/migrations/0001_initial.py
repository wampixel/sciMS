# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_fname', models.CharField(max_length=50)),
                ('user_lname', models.CharField(max_length=50)),
                ('user_pseudo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_pass', models.CharField(default='password', max_length=32)),
            ],
        ),
    ]
