from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=128)
    released = models.DateField()
    genre = models.CharField(max_length=256)
    director = models.CharField(max_length=128)
    writer = models.CharField(max_length=128)
    actors = models.CharField(max_length=256)
    country = models.CharField(max_length=128)
    awards = models.CharField(max_length=256)
    mox_office = models.FloatField(blank=True, null=True)
    imdb_rating = models.FloatField(blank=True, null=True)
    language = models.CharField(max_length=128, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    rated = models.CharField(max_length=32, blank=True, null=True)
    runtime = models.DurationField(blank=True, null=True)
    my_favorite = models.BooleanField(default=False)
