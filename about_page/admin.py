from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About_page



@admin.register(About_page)
class AboutPage(SummernoteModelAdmin):
    summernote_fields = ('title', 'body_content')


# Register your models here.
