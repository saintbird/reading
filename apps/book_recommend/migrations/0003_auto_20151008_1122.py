# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommend', '0002_auto_20151007_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='intro',
            new_name='authorIntro',
        ),
        migrations.RemoveField(
            model_name='bookinfo',
            name='detailUrl',
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='author',
            field=models.CharField(default='author_intro', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='summary',
            field=models.CharField(default='summary', max_length=1000),
            preserve_default=False,
        ),
    ]
