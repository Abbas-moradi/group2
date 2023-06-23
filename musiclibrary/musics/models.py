from django.db import models

class Artist(models.Model):
    name = models.CharField(unique=True, max_length=150)
    genre = models.CharField(max_length=50)
    bio = models.TextField()

class Album(models.Model):
    title = models.CharField(unique=True, max_length=70)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='media/')
    description = models.TextField()