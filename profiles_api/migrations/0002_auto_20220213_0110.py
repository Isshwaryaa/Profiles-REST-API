# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-02-13 01:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
