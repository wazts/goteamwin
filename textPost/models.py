import os
from django.db import models
from django.conf import settings

from post.models import BasePost

# Create your models here.
class TextPost(BasePost):
    
    post_type = "text"
    
    # templates
    body_detail_template = 'textPost/post.html'
    feed_description_template = 'textPost/feed_detail.html'
    list_template = 'textPost/list.html'
    body_list_template = 'textPost/body_list.html'
    
    # fields
    body = models.TextField('Post body')
    
    @models.permalink
    def get_absolute_url(self):
        return ('text_details', None, { 'slug': self.slug })