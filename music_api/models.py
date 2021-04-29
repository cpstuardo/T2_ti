from django.db import models

# Create your models here.

class Artist(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=100)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    albums_url = models.URLField()
    tracks_url = models.URLField()
    self_url = models.URLField()

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    id = models.CharField(primary_key=True, editable=False, max_length=100)
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    artist_url = models.URLField()
    tracks_url = models.URLField()
    self_url = models.URLField()

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    id = models.CharField(primary_key=True, editable=False, max_length=100)
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    times_played = models.IntegerField()
    artist_url = models.URLField()
    album_url = models.URLField()
    self_url = models.URLField()
