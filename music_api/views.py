from django.shortcuts import render
from django.views import View
from django.db.models import F
from base64 import b64encode
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer

# Create your views here.
@api_view(['POST','GET'])
def artists(request):
    if request.method == 'POST':
        data = request.data
        encoded_id = b64encode(data['name'].encode()).decode('utf-8')[:22]
        if Artist.objects.filter(id= encoded_id).exists(): 
            artist = Artist.objects.filter(id= encoded_id)
            serializer = ArtistSerializer(artist)
            artist.save()
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)
        artist = Artist.objects.create(id= encoded_id, name=data['name'], age=int(data['age']), albums_url= f'/artists/{encoded_id}/albums', tracks_url= f'/artists/{encoded_id}/tracks', self_url= f'/artists/{encoded_id}')
        if artist: 
            serializer = ArtistSerializer(artist)
            artist.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many= True)
        return Response(serializer.data)

@api_view(['GET','DELETE'])            
def artist_id(request, artist_id):
    if request.method == 'GET':
        if Artist.objects.filter(id=artist_id).exists():
            artist = Artist.objects.filter(id=artist_id)
            serializer = ArtistSerializer(artist[0])
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        if Artist.objects.filter(id=artist_id).exists():
            artist = Artist.objects.filter(id=artist_id).delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST']) 
def artists_albums(request, artist_id):
    if request.method == 'POST':
        data = request.data
        nombre = data['name']
        encoder = f'{nombre}:{artist_id}'
        encoded_id = b64encode(encoder.encode()).decode('utf-8')[:22]
        if not(Artist.objects.filter(id= artist_id).exists()): # Si el artist no existe
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if Album.objects.filter(id= encoded_id).exists(): # Si el album ya existe 
            album = Album.objects.filter(id= encoded_id)[0] 
            serializer = AlbumSerializer(album)
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)
        album = Album.objects.create(id= encoded_id, artist_id= artist_id, name=data['name'], genre=data['genre'], artist_url= f'/artists/{artist_id}', tracks_url= f'/albums/{encoded_id}/tracks', self_url= f'/albums/{encoded_id}')
        if album: 
            serializer = AlbumSerializer(album)
            album.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        if not(Artist.objects.filter(id= artist_id).exists()): # Si el artist no existe
            return Response(status=status.HTTP_404_NOT_FOUND)
        albums = Album.objects.filter(artist_id= artist_id)
        serializer = AlbumSerializer(albums, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET']) 
def artists_tracks(request, artist_id):
    if request.method == 'GET':
        if not(Artist.objects.filter(id= artist_id).exists()): # Si el artist no existe
            return Response(status=status.HTTP_404_NOT_FOUND)
        tracks_artista = Track.objects.filter(album__artist=artist_id)
        serializer = TrackSerializer(tracks_artista, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET']) 
def albums(request):
    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET', 'DELETE']) 
def album_id(request, album_id):
    if request.method == 'GET':
        if Album.objects.filter(id=album_id).exists():
            album = Album.objects.filter(id=album_id)
            serializer = AlbumSerializer(album[0])
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        if Album.objects.filter(id=album_id).exists():
            album = Album.objects.filter(id=album_id).delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)     

@api_view(['GET','POST']) 
def albums_tracks(request, album_id):
    if request.method == 'POST':
        data = request.data
        nombre = data['name']
        encoder = f'{nombre}:{album_id}'
        encoded_id = b64encode(encoder.encode()).decode('utf-8')[:22]
        if not(Album.objects.filter(id= album_id).exists()): # Si el album no existe
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        album = Album.objects.filter(id= album_id)[0]
        if Track.objects.filter(id= encoded_id).exists(): # Si la canción ya existe 
            track = Track.objects.filter(id= encoded_id)[0]
            serializer = TrackSerializer(track)
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)
        track = Track.objects.create(id= encoded_id, album_id= album_id, name=data['name'], duration=float(data['duration']), times_played= 0, artist_url= f'/artists/{album.artist_id}', album_url= f'/albums/{album_id}', self_url= f'/tracks/{encoded_id}')
        if track: 
            serializer = TrackSerializer(track)
            track.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        if not(Album.objects.filter(id= album_id).exists()): # Si el album no existe
            return Response(status=status.HTTP_404_NOT_FOUND)
        tracks = Track.objects.filter(album_id= album_id)
        serializer = TrackSerializer(tracks, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET']) 
def tracks(request):
    if request.method == 'GET':
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['GET', 'DELETE']) 
def track_id(request, track_id):
    if request.method == 'GET':
        if Track.objects.filter(id=track_id).exists():
            track = Track.objects.filter(id=track_id)
            serializer = TrackSerializer(track[0])
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        if Track.objects.filter(id=track_id).exists():
            track = Track.objects.filter(id=track_id).delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)   

@api_view(['PUT']) 
def artists_albums_play(request, artist_id):
    if request.method == 'PUT':
        if not(Artist.objects.filter(id= artist_id).exists()): # Si el artista no existe
            return Response(status=status.HTTP_404_NOT_FOUND)
        Track.objects.filter(album__artist=artist_id).update(times_played=F('times_played') + 1)
        return Response(status= status.HTTP_200_OK)

@api_view(['PUT']) 
def albums_tracks_play(request, album_id):
    if request.method == 'PUT':
        if not(Album.objects.filter(id= album_id).exists()): # Si el album no existe
            return Response(status=status.HTTP_404_NOT_FOUND)
        Track.objects.filter(album_id=album_id).update(times_played=F('times_played') + 1)
        return Response(status= status.HTTP_200_OK)

@api_view(['PUT']) 
def track_play(request, track_id):
    if request.method == 'PUT':
        if not(Track.objects.filter(id= track_id).exists()): # Si el track no existe
            return Response(status=status.HTTP_404_NOT_FOUND)
        Track.objects.filter(id=track_id).update(times_played=F('times_played') + 1)
        return Response(status= status.HTTP_200_OK)
