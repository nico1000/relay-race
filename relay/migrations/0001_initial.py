# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='EventStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.PositiveSmallIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relay.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Number')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('distance', models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Distance [km]')),
            ],
        ),
        migrations.AddField(
            model_name='eventstage',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relay.Stage'),
        ),
        migrations.AddField(
            model_name='event',
            name='stages',
            field=models.ManyToManyField(through='relay.EventStage', to='relay.Stage'),
        ),
    ]