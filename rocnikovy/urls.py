"""
URL configuration for rocnikovy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),

    path('authors/', views.author_list, name='author_list'),
    path('author/new/', views.author_new, name='author_new'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('author/<int:pk>/delete/', views.author_delete, name='author_delete'),

    path('genres/', views.genre_list, name='genre_list'),
    path('genre/new/', views.genre_edit, name='genre_new'),
    path('genre/<int:pk>/', views.genre_detail, name='genre_detail'),
    path('genre/<int:pk>/edit/', views.genre_edit, name='genre_edit'),
    path('genre/<int:pk>/delete/', views.genre_delete, name='genre_delete'),

    path('albums/', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/new/', views.album_edit, name='album_new'),
    path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),

    path('songs/', views.song_list, name='song_list'),
    path('song/new/', views.song_new, name='song_new'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('song/<int:pk>/edit/', views.song_edit, name='song_edit'),
    path('song/<int:pk>/delete/', views.song_delete, name='song_delete'),

    path('playlists/', views.playlist_list, name='playlist_list'),
    path('playlist/new/', views.playlist_edit, name='playlist_new'),
    path('playlist/<int:pk>/edit/', views.playlist_edit, name='playlist_edit'),
    path('playlist/<int:pk>/delete/', views.playlist_delete, name='playlist_delete'),
]
