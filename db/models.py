from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="upload",)


playlisttype_choices = [
("Information", "staticImage"),
("Diashow", "diashow1"),
]
class Playlist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class SpecialPlaylist(models.Model):
    name = models.CharField(max_length=50, unique=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return f"{self.name}: {self.playlist}"


class PlaylistHasImages(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.playlist}: {self.image}"


eventtype_choices = [
("set current Playlist", "setPlaylist"),
("stop current Playlist", "stopPlaylist"),
]
class PlannedPlaylistEvent():
    eventtype = models.CharField(max_length=100, choices=eventtype_choices)
    repeating = models.BooleanField(default = False)
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    time_end = models.TimeField(auto_now=False, auto_now_add=False)
    startdate = models.DateField(auto_now=False, auto_now_add=False)
    enddate = models.DateField(auto_now=False, auto_now_add=False, default=startdate)