# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-15 16:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0003_show_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='release_date',
        ),
    ]
