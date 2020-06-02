from django.shortcuts import render

# Create your views here.
from .models import Artwork
from .serializers import ArtworkSerializer
from rest_framework import generics


class ArtworkList(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

