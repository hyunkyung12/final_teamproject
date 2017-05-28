from django.contrib import admin
from .models import Univs

class UnivsAdminDisplay(admin.ModelAdmin):
    list_display = ('uni_number', 'uni_name')
    search_fields = ['uni_number']

admin.site.register(Univs, UnivsAdminDisplay)
