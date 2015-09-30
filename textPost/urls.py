"""
The URL patterns for the text based posts.
"""

from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic import TemplateView
from django.conf import settings

from textPost.models import TextPost

from textPost import views

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=TextPost.objects.order_by('-date_pub'),
            context_object_name='posts',
            paginate_by=settings.PAGINATION_LIMIT,
            template_name='textPost/index.html'),
            name='text_posts_index'),
    url(r'^(?P<slug>.+)$', views.text_post_view, name='text_post_single'),
)