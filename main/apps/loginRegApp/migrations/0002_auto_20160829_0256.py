# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 02:56
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('UserManager', django.db.models.manager.Manager()),
            ],
        ),
    ]