# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-10 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default=1000),
            preserve_default=False,
        ),
    ]