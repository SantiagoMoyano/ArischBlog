# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150806_1808'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
    ]
