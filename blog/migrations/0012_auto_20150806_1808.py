# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_mensajes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mail', models.CharField(max_length=100, verbose_name='Mail')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('asunto', models.TextField(verbose_name='Asunto')),
            ],
        ),
        migrations.AlterModelOptions(
            name='mensajes',
            options={'ordering': ['-fecha'], 'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
    ]
