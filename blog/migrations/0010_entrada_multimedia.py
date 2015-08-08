# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150804_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='multimedia',
            field=models.FileField(upload_to=b'/multimedia', verbose_name='Multimedia', blank=True),
        ),
    ]
