# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('rates', models.CharField(max_length=10)),
                ('votes', models.CharField(max_length=10)),
                ('imgUrl', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=10)),
            ],
        ),
    ]
