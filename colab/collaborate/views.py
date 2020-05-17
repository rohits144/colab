from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CollaborateSerializer
from .models import Collaborate


class CollaborateViewset(viewsets.ModelViewSet):
    serializer_class = CollaborateSerializer
    queryset = Collaborate.objects.all()

    class Meta:
        model = Collaborate
