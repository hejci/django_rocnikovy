from django import forms
from .models import Author, Genre, Album, Song, Playlist


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'birth_date']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'release_date', 'genres']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'genres']


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'songs']
