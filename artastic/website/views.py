from django.shortcuts import render

# Create your views here.
from .models import Artwork
from .serializers import ArtworkSerializer
from rest_framework import generics


class ArtworkList(generics.ListCreateAPIView):
    serializer_class = ArtworkSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Artwork.objects.all()
            artwork_name = self.request.GET.get('q', None)
            if artwork_name is not None:
                queryset = queryset.filter(name__contains=artwork_name)
            return queryset
