from rest_framework import serializers
from music_api.models import Artist, Album, Track

class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.CharField(source='albums_url')
    tracks = serializers.CharField(source='tracks_url')
    self = serializers.CharField(source='self_url')
    class Meta:
        model = Artist
        fields = ['id', 'name', 'age', 'albums', 'tracks', 'self']

class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(source='artist_url')
    tracks = serializers.CharField(source='tracks_url')
    self = serializers.CharField(source='self_url')
    class Meta:
        model = Album
        fields = ['id', 'artist_id', 'name', 'genre', 'artist', 'tracks', 'self']

class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.CharField(source='artist_url')
    album = serializers.CharField(source='album_url')
    self = serializers.CharField(source='self_url')
    class Meta:
        model = Track
        fields = ['id', 'album_id', 'name', 'duration', 'times_played', 'artist', 'album', 'self'] 