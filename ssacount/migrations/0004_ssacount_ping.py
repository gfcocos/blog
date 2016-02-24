# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssacount', '0003_ssacount'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssacount',
            name='ping',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
