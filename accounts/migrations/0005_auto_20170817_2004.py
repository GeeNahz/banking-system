# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170817_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]