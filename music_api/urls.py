from django.urls import path
from .views import artists, artist_id, artists_albums, albums, album_id, albums_tracks, tracks, track_id, artists_tracks, artists_albums_play, albums_tracks_play, track_play

urlpatterns = [
    path('artists', artists), 
    path('artists/<artist_id>', artist_id),
    path('artists/<artist_id>/albums', artists_albums),
    path('artists/<artist_id>/tracks', artists_tracks),
    path('albums', albums),
    path('albums/<album_id>', album_id),
    path('albums/<album_id>/tracks', albums_tracks),
    path('tracks', tracks),
    path('tracks/<track_id>', track_id),
    path('artists/<artist_id>/albums/play', artists_albums_play),
    path('albums/<album_id>/tracks/play', albums_tracks_play),
    path('tracks/<track_id>/play', track_play),
]