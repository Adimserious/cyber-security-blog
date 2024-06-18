from django.contrib import admin
from .models import Blog_post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Blog_post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created')
    search_fields = ['title', 'body_content']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body_content',)

# Register your models here.

