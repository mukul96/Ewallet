# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-12 04:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='user',
            new_name='person',
        ),
    ]