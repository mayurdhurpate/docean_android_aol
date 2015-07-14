# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0007_message_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='url',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
