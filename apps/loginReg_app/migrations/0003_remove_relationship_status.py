# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 22:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg_app', '0002_auto_20171024_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='status',
        ),
    ]
