# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20171104_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default=None, upload_to='project_images'),
        ),
    ]