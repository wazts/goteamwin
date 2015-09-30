"""
The views associated with the GoTeamWin website
"""

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from post.models import BasePost
from series.models import SeriesPost

def handler404(request):
    return render(request, '404.html', status_code=404)


def handler500(request):
    return render(request, '500.html', status_code=500)

def home(request):
    """ Return the home page
    """
    posts = BasePost.objects.all().order_by('-date_pub')
    recent_media = SeriesPost.objects.all().order_by('-date_pub')[:3]
    paginator = Paginator(posts, settings.PAGINATION_LIMIT)

    page_num = request.GET.get('page', 1)
    
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)
    
    return render(request, 'index.html', {'posts': posts, 'page': page, 'recent_media': recent_media})