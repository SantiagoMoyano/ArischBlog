# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150804_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.CharField(default=b'img/skyrim.jpg', max_length=1024, verbose_name='URL de la Imagen del Post'),
        ),
    ]
