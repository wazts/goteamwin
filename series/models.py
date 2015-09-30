import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from post.models import BasePost

class Series(models.Model):
    """
    A group of media that has the same show.
    """
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=False)
    description = models.TextField()
    
    def __unicode__(self):
        return '%s' % self.title
        
class Season(models.Model):
    """
    A group of episodes from a series.
    """
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    number = models.IntegerField()
    series = models.ForeignKey(Series, related_name='seasons')
    slug = models.SlugField(max_length=100, unique=True, blank=False)
    
    def __unicode__(self):
        return '%s' % self.series + ' ' + self.title
        
class SeriesPost(BasePost):
    """
    A post pertaining to a series. It can be media of any type
    """
    post_type = "series"
    
    # templates
    body_detail_template = 'series/post.html'
    feed_description_template = 'series/feed_detail.html'
    list_template = 'series/list.html'
    body_list_template = 'series/body_list.html'
    
    # fields
    series = models.ForeignKey(Series, related_name='episodes')
    season = models.ForeignKey(Season, related_name='episodes', blank=True, null=True)
    actors = models.ManyToManyField(User)
    episode_number = models.IntegerField()
    description = models.TextField()