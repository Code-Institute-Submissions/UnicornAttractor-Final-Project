# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-15 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_auto_20190215_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('In Development', 'In Development'), ('Done', 'Done')], default='Not Started', max_length=1),
        ),
    ]
