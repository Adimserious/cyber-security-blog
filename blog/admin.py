from django.contrib import admin
from .models import Category, Blog_post, Comment, FeaturedPost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blog_post)
class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created', 'featured')
    search_fields = ['title', 'body_content']
    list_filter = ('status', 'created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body_content',)


@admin.register(FeaturedPost)
class FeaturedPostAdmin(admin.ModelAdmin):
    list_display = ('post', 'featured_on', 'highlight_until', 'is_active')
    list_filter = ('is_active', 'featured_on')
    search_fields = ('post__title', 'post__author__username')
    ordering = ['-featured_on']
    date_hierarchy = 'featured_on'


admin.site.register(Category)
admin.site.register(Comment)
