# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='pds',
            field=models.FloatField(),
        ),
    ]