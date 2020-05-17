from django.db import models

from artist.models import Artist


class Collaborate(models.Model):

    artist1 = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artist1")
    artist2 = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artist2")
    upvotes = models.IntegerField(default=0)
    creation_date = models.TimeField(auto_now_add=True)