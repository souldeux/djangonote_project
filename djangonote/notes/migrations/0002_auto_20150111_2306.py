# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(related_name=b'notes', to=b'notes.Tag', blank=True),
        ),
    ]
