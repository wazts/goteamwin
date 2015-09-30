# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('seriespost_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='series.SeriesPost')),
                ('embeded_video', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'abstract': False,
            },
            bases=('series.seriespost',),
        ),
    ]
