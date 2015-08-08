# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150804_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.CharField(max_length=1024, verbose_name='URL de la Imagen del Post'),
        ),
    ]
