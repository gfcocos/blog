# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssacount', '0002_article_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSAcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.CharField(max_length=50)),
                ('server_port', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
