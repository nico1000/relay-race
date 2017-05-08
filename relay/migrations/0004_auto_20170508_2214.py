# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relay', '0003_auto_20170508_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time_estimated', models.DurationField()),
                ('event_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relay.EventStage')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stage',
            name='distance',
            field=models.DecimalField(decimal_places=3, help_text='distance in kilometers', max_digits=5),
        ),
        migrations.AddField(
            model_name='team',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relay.Event'),
        ),
        migrations.AddField(
            model_name='runner',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relay.Team'),
        ),
    ]
