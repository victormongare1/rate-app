# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-07 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='overall_score',
            field=models.PositiveIntegerField(null=True),
        ),
    ]