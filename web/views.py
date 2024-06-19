from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Genre, Album, Song, Playlist
from .forms import AuthorForm, SongForm, PlaylistForm, AlbumForm


# Author views
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})


def author_edit(request, pk=None):
    if pk:
        author = get_object_or_404(Author, pk=pk)
    else:
        author = Author()
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_edit.html', {'form': form})


# Genre views
def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})


def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return render(request, 'genre_detail.html', {'genre': genre})


# Album views
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})


def album_edit(request, pk=None):
    if pk:
        album = get_object_or_404(Album, pk=pk)
    else:
        album = Album()
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            form.save_m2m()  # Save the many-to-many data for genres
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_edit.html', {'form': form})


# Song views
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})


def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'song_detail.html', {'song': song})


def song_edit(request, pk=None):
    if pk:
        song = get_object_or_404(Song, pk=pk)
    else:
        song = Song()
    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            form.save_m2m()  # Save the many-to-many data for genres
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'song_edit.html', {'form': form})


# Playlist views
def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlist_list.html', {'playlists': playlists})


def playlist_edit(request, pk=None):
    if pk:
        playlist = get_object_or_404(Playlist, pk=pk)
    else:
        playlist = Playlist()
    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.save()
            form.save_m2m()  # Save the many-to-many data for songs
            return redirect('playlist_detail', pk=playlist.pk)
    else:
        form = PlaylistForm(instance=playlist)
    return render(request, 'playlist_edit.html', {'form': form})


def landing_page(request):
    return render(request, 'landing_page.html')
