# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-08 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='./images/default-avatar.png', null=True, upload_to='images/'),
        ),
    ]
