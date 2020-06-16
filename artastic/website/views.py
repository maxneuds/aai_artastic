from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import website.services as utils
import json


class ArtworkList(APIView):
    def post(self, request):
        data = request.data
        print(data)
        informations = utils.get_artwork(data['data'])
        return Response(informations)


class GetArtist(APIView):
    def post(self, request):
        data = request.data
        print(data)
        informations = utils.get_artist(data['data'])
        return Response(informations)
