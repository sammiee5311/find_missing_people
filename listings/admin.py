from django.contrib import admin
from .models import MissingPeople


class MissingPeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_found', 'missing_date')
    list_display_links = ('id', 'name')
    list_editable = ('is_found',)
    search_fields = ('name', 'description', 'address', 'city', 'state')
    list_per_page = 25

admin.site.register(MissingPeople, MissingPeopleAdmin)

