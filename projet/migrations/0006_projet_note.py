# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0005_merge_20190121_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='note',
            field=models.IntegerField(default=0),
        ),
    ]
