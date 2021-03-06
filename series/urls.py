"""
The URL patterns for the text based posts.
"""

from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic import TemplateView
from django.conf import settings

from series.models import Series

from series import views

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Series.objects.order_by('title'),
            context_object_name='series',
            template_name='series/index.html'),
            name='series_all_index'),
    url(r'^(?P<sSlug>.+)/$', views.series_episodes_view, name='series_episodes'),
    url(r'^(?P<sSlug>.+)/(?P<eSlug>.+)$', views.series_episode_single_view, name='series_episode_single')
)