# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 00:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20170131_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='video',
        ),
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
            preserve_default=False,
        ),
    ]
