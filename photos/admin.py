from django.contrib import admin
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields": ['title', 'img', 'created_date', 'published_date']})]
    list_display = ['title']
    ordering = ['title']


admin.site.register(Photo, PhotoAdmin)
