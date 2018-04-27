# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('is_male', models.BooleanField(default=False)),
                ('birth_date', models.DateField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]