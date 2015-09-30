from django.contrib import admin
from post.models import BasePost

class BasePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date_pub', 'date_created', 'date_last_modified')
    list_filter = ['date_pub']
    date_hierarchy = 'date_pub'
    
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(BasePost, BasePostAdmin)