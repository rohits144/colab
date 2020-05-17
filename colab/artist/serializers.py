from rest_framework import serializers

from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["name", "is_band"]

    def create(self, validated_data):
        artist = Artist(
            name=validated_data["name"].upper(),
            is_band=validated_data["is_band"]
        )
        artist.save()
        return artist