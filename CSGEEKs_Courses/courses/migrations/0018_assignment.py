# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_auto_20170131_0300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('by', models.CharField(default='', max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
    ]
