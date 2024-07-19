from django.contrib import admin
from .models import Blog_post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Blog_post)
class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created')
    search_fields = ['title', 'body_content']
    list_filter = ('status', 'created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body_content',)


# Register your models here.


admin.site.register(Comment)
