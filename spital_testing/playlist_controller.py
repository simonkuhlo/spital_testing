from . import models
from django.core.exceptions import ObjectDoesNotExist

class SpecialPlaylist():
    def __init__(self, name) -> None:
        try:
            self.database_object:models.SpecialPlaylist = models.SpecialPlaylist.objects.get(name=name)
        except ObjectDoesNotExist:
            self.database_object:models.SpecialPlaylist = models.SpecialPlaylist(name=name).save()
    def set_playlist(self, Playlist:models.SpecialPlaylist):
        self.playlist = Playlist

    def get_playlist(self) -> models.SpecialPlaylist:
        return self.playlist



current_playlist = SpecialPlaylist(name="current")

main_playlist = SpecialPlaylist(name="main")


    



