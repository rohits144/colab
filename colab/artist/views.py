from django.shortcuts import render
from rest_framework import viewsets

from .models import Artist
from .serializers import ArtistSerializer


class ArtistViewset(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    class Meta:
        model = Artist

