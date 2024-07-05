from django.contrib import admin
from .models import RequestContact

# Register your models here.
@admin.register(RequestContact)
class RequestContactAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
