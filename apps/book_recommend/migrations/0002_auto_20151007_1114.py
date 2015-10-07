# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='detailUrl',
            field=models.CharField(default='detail_url', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='intro',
            field=models.CharField(default='intro', max_length=1000),
            preserve_default=False,
        ),
    ]
