from django.contrib import admin
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from video.models import Video

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)
