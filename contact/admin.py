from django.contrib import admin
from .models import RequestContact


# Contact Admin registration.
@admin.register(RequestContact)
class RequestContactAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
