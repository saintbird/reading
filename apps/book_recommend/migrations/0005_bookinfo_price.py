# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommend', '0004_maintag_subtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='price',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
