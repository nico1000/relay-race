# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='number',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='title',
        ),
        migrations.AddField(
            model_name='stage',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stage',
            name='distance',
            field=models.DecimalField(decimal_places=3, help_text='distance in kilometers', max_digits=5, verbose_name='distance'),
        ),
    ]
