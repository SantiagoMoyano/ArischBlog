# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150804_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.URLField(default=b'static/img/skyrim.jpg', max_length=1024, verbose_name='URL de la Imagen del Post'),
        ),
    ]
