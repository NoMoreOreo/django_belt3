# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogReg', '0004_auto_20170127_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=None, max_length=100),
        ),
    ]