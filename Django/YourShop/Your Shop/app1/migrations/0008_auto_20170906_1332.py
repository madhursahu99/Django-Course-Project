# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 08:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_review'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='review',
            new_name='item_review',
        ),
    ]
