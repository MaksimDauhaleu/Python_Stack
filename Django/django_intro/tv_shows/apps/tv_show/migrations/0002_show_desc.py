# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-15 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='desc',
            field=models.CharField(default=1000, max_length=1000),
            preserve_default=False,
        ),
    ]
