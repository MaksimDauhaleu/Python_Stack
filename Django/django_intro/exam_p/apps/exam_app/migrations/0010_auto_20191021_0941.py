# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-21 16:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0009_remove_other_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Other',
            new_name='Others',
        ),
    ]
