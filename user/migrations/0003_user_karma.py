# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181206_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='karma',
            field=models.IntegerField(default=0),
        ),
    ]
