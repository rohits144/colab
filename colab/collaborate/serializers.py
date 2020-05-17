from rest_framework import serializers

from .models import Collaborate


class CollaborateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborate
        fields = "__all__"
