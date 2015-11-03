# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommend', '0005_bookinfo_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='bookid',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='isbn10',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='isbn13',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
