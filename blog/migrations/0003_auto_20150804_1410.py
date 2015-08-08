# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150804_1401'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacto',
        ),
        migrations.RenameField(
            model_name='entrada',
            old_name='categoria',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.FileField(default=b'null', upload_to=b'imagenesdepost', verbose_name='Imagen del Post'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre del Tag'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Habilitado'),
        ),
    ]
