# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_created',
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
