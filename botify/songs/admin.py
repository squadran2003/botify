from django.contrib import admin

from .models import Song, Like, Comment, TempThumbnail

admin.site.register(Song)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(TempThumbnail)
