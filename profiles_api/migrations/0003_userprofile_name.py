# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-02-13 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20220213_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='Isha', max_length=255),
        ),
    ]
