# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-20 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0018_auto_20180619_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpus',
            name='version',
            field=models.CharField(max_length=200, null=True, verbose_name='Version'),
        ),
    ]
