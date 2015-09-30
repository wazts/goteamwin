from django.shortcuts import render
from series.models import SeriesPost
from django.shortcuts import get_object_or_404

def series_episodes_view(request, sSlug):
	pass

def series_episode_single_view(request, sSlug, eSlug):
	
	episode = get_object_or_404(SeriesPost, series__slug=sSlug, slug=eSlug)
	
	return render(  request, 
					episode.single_template, 
					{
						'episode': episode, 
					})