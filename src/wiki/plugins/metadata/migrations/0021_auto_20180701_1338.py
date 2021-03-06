# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-01 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0020_auto_20180621_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corpus',
            name='id',
        ),
        migrations.AddField(
            model_name='corpus',
            name='simplemetadata_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metadata.SimpleMetadata'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ptokenannotation',
            name='gov_head_index',
            field=models.PositiveIntegerField(max_length=200, null=True, verbose_name='Governor Index'),
        ),
        migrations.AddField(
            model_name='ptokenannotation',
            name='is_abbr',
            field=models.BooleanField(default=False, verbose_name='Abbreviation?'),
        ),
        migrations.AddField(
            model_name='ptokenannotation',
            name='is_typo',
            field=models.BooleanField(default=False, verbose_name='Typo?'),
        ),
        migrations.AddField(
            model_name='ptokenannotation',
            name='obj_head_index',
            field=models.PositiveIntegerField(max_length=200, null=True, verbose_name='Object Index'),
        ),
        migrations.AlterField(
            model_name='ptokenannotation',
            name='adposition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='metadata.Adposition'),
        ),
        migrations.AlterField(
            model_name='ptokenannotation',
            name='construal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='metadata.Construal'),
        ),
        migrations.AlterField(
            model_name='ptokenannotation',
            name='gov_head',
            field=models.CharField(max_length=200, null=True, verbose_name='Governor Head'),
        ),
        migrations.AlterField(
            model_name='ptokenannotation',
            name='gov_obj_syntax',
            field=models.CharField(max_length=200, null=True, verbose_name='Governor-Object Syntax'),
        ),
        migrations.AlterField(
            model_name='ptokenannotation',
            name='obj_head',
            field=models.CharField(max_length=200, null=True, verbose_name='Object Head'),
        ),
        migrations.AlterField(
            model_name='ptokenannotation',
            name='sentence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='metadata.CorpusSentence'),
        ),
        migrations.AlterField(
            model_name='ptokenannotation',
            name='usage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='metadata.Usage'),
        ),
    ]
