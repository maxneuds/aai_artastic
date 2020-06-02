from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ('name', 'artist', 'created_at', 'updated_at')