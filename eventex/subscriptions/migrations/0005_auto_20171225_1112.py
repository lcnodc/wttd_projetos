# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-25 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_auto_20171220_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='telefone'),
        ),
    ]
