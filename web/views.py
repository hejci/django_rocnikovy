from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Genre, Album, Song, Playlist
from .forms import AuthorForm, SongForm, PlaylistForm, AlbumForm, GenreForm


# Author views
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author/author_detail.html', {'author': author})


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
    return render(request, 'author/author_edit.html', {'form': form})


def author_new(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  # Replace 'author_list' with your actual URL name for author list view
    else:
        form = AuthorForm()
    return render(request, 'author/author_edit.html', {'form': form})


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')  # Replace 'author_list' with your actual URL name for author list view
    return render(request, 'author/author_delete.html', {'author': author})


# Genre views
def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre/genre_list.html', {'genres': genres})


def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return render(request, 'genre/genre_detail.html', {'genre': genre})


def genre_edit(request, pk=None):
    if pk:
        genre = get_object_or_404(Genre, pk=pk)
    else:
        genre = Genre()
    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.save()
            return redirect('genre_detail', pk=genre.pk)
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genre/genre_edit.html', {'form': form})


def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        genre.delete()
        return redirect('genre_list')  # Replace 'genre_list' with your actual URL name for genre list view
    return render(request, 'genre/genre_delete.html', {'genre': genre})


# Album views
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album/album_detail.html', {'album': album})


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
    return render(request, 'album/album_edit.html', {'form': form})


def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'album/album_delete.html', {'album': album})


def song_new(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'song/song_edit.html', {'form': form})


# Song views
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song/song_list.html', {'songs': songs})


def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'song/song_detail.html', {'song': song})


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
    return render(request, 'song/song_edit.html', {'form': form})


def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')  # Replace 'song_list' with your actual URL name for song list view
    return render(request, 'song/song_delete.html', {'song': song})


# Playlist views
def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlist/playlist_list.html', {'playlists': playlists})


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
    return render(request, 'playlist/playlist_edit.html', {'form': form})


def playlist_delete(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    if request.method == 'POST':
        playlist.delete()
        return redirect('playlist_list')  # Replace 'playlist_list' with your actual URL name for playlist list view
    return render(request, 'playlist/playlist_delete.html', {'playlist': playlist})


def landing_page(request):
    return render(request, 'landing_page.html')
