from django.contrib import admin
from post.admin import BasePostAdmin
from textPost.models import TextPost

class TextPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_pub', 'date_created', 'date_last_modified')
    list_filter = ['date_pub', 'title']
    date_hierarchy = 'date_pub'
    
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(TextPost, TextPostAdmin)