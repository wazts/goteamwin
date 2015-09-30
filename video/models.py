from django.db import models

from series.models import SeriesPost
from embed_video.fields import EmbedVideoField
from embed_video.backends import detect_backend

# Create your models here.
class Video(SeriesPost):
    """
    A post that pertains to the videos. Could be said it is the same as an
    episode.
    """
    
    post_type = "video"
    
    # templates
    single_template = 'video/single.html'
    body_detail_template = 'video/detail.html'
    feed_description_template = 'video/feed_detail.html'
    list_template = 'video/list.html'
    body_list_template = 'video/body_list.html'
    featured_home_template = 'video/featured_home.html'
    
    # Fields
    embeded_video = EmbedVideoField()
    
    def get_featured_image_url(self):
        
        imageURL = ""
        if self.featured_image:
            imageURL = self.featured_image.url
        elif self.embeded_video:
            try:
                imageURL = detect_backend(self.embeded_video).thumbnail
            except Exception, e:
                imageURL = ""
            
        return imageURL