from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=255, help_text= 'Zadej autora', error_messages='Musí být zadáno jméno autora')
    bio = models.TextField(blank=True, null=True, help_text= 'Informace o autorovi')
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text= 'Zadej žánr', error_messages={ 'max_length': 'Maximální délka je 100 znaků',
                                                                                                   'unique': 'Žánry se nesmí opakovat'})

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255, help_text= 'Zadej jméno alba')
    artist = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='album')
    release_date = models.DateField(help_text= 'Kdy bylo album vydáno')
    genres = models.ManyToManyField(Genre, related_name='albums')

    def __str__(self):
        return f"{self.title} by {self.artist.name}"


class Song(models.Model):
    title = models.CharField(max_length=255, help_text= 'Zadej název skladby')
    artist = models.CharField(max_length=255, help_text= 'Zadej autora')
    album = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=10)
    song_file = models.FileField(upload_to='songs')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='songs')
    genres = models.ManyToManyField(Genre, related_name='songs')

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, related_name='playlists')

    def __str__(self):
        return f"{self.name} by {self.user.username}"