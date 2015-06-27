# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0002_noti'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('token', models.CharField(max_length=1000)),
                ('message_id', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
    ]
