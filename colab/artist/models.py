from django.db import models


class Artist(models.Model):
    """ this class will store detail of indivisual Artist or a band"""

    name = models.CharField(blank=False, unique=True, max_length=100, null=False)
    is_band = models.BooleanField(blank=True)
