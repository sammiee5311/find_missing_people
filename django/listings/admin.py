from django.contrib import admin
from .models import Listing

class ListigAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_found', 'missing_date', 'requestor')
    list_display_links = ('id', 'name')
    list_filter = ('requestor',)
    list_editable = ('is_found',)
    search_fields = ('name', 'description', 'address', 'city', 'state')
    list_per_page = 25


admin.site.register(Listing, ListigAdmin)
