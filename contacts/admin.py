from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_name', 'missing_person_name', 'email', 'contact_date')
    list_display = ('id', 'from_name')
    search_fields = ('from_name', 'email', 'missing_person_name')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
