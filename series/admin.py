from django.contrib import admin
from series.models import Series, SeriesPost, Season
# Register your models here.
admin.site.register(Series)
admin.site.register(SeriesPost)
admin.site.register(Season)