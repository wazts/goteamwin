import os
from django.db import models
from polymorphic import PolymorphicModel
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Featured image path
def get_featured_img_path(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'featured/%s%s' % (instance.slug.replace(" ", "_").lower(), filename_ext)

# Create your models here.

class BasePost (PolymorphicModel):
    
    # templates
    list_template = 'post/list.html'
    single_template = 'post/single.html'
    body_detail_template = 'post/body_detail.html'
    body_list_template = 'post/body_list.html'
    feed_title_template = 'post/feed_title.html'
    feed_description_template = 'post/feed_description.html'
    featured_home_template = 'post/featured_home.html'
    
    # Type
    post_type="base"
    
    # fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, blank=False)
    author = models.ForeignKey(User, related_name='posts')
    comments_on = models.BooleanField(default=True)
    tags = TaggableManager(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    date_pub = models.DateTimeField ('date published')
    
    parent = models.ForeignKey('BasePost', related_name='children', blank=True, null=True)
    
    featured_post = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to=get_featured_img_path, blank=True)
    
    def upcast (self):
        return upcast(self)
        
    def __unicode__(self):
        return '%s' % self.title
        
    def get_disqus_id(self):
        return '%s-%s' % (self.post_type, self.slug)