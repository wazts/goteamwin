# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('number', models.IntegerField()),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SeriesPost',
            fields=[
                ('basepost_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='post.BasePost')),
                ('episode_number', models.IntegerField()),
                ('description', models.TextField()),
                ('actors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('season', models.ForeignKey(related_name='episodes', blank=True, to='series.Season', null=True)),
                ('series', models.ForeignKey(related_name='episodes', to='series.Series')),
            ],
            options={
                'abstract': False,
            },
            bases=('post.basepost',),
        ),
        migrations.AddField(
            model_name='season',
            name='series',
            field=models.ForeignKey(related_name='seasons', to='series.Series'),
        ),
    ]
