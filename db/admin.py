from django.contrib import admin
from . import models


admin.site.register(models.Playlist)
admin.site.register(models.SpecialPlaylist)
admin.site.register(models.PlaylistHasImages)
admin.site.register(models.Image)