# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0006_message_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='topic',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
