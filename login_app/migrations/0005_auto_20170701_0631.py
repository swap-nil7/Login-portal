# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_auto_20170630_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstats',
            old_name='userdetails',
            new_name='user',
        ),
    ]