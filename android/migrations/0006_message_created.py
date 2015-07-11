# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0005_auto_20150627_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
