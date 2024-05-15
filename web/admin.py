from django.contrib import admin
from .models import Author, Genre, Album, Song, Playlist

# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)