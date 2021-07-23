from django.contrib import admin

from .models import Video, ImagesFromVideo


class ImagesFromVideoAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'missing_person_id')
    list_display_links = ('user_id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Video)
admin.site.register(ImagesFromVideo, ImagesFromVideoAdmin)