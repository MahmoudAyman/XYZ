# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 00:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20170131_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.Video'),
            preserve_default=False,
        ),
    ]
