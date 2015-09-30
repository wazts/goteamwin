# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextPost',
            fields=[
                ('basepost_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='post.BasePost')),
                ('body', models.TextField(verbose_name=b'Post body')),
            ],
            options={
                'abstract': False,
            },
            bases=('post.basepost',),
        ),
    ]
