# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-10 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_dojo_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='state',
            field=models.TextField(),
        ),
    ]
