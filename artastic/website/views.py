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
        information = utils.get_artwork(data)
        return Response(information)


class ArtworkByQ(APIView):
    def post(self, request):
        data = request.data
        information = utils.get_artwork_by_Q(data)
        return Response(information)


class GetArtist(APIView):
    def post(self, request):
        data = request.data
        print(data)
        information = utils.get_artist(data)
        return Response(information)


class GetLocation(APIView):
    def post(self, request):
        data = request.data
        print(data)
        information = utils.get_location(data)
        return Response(information)


class GetMovement(APIView):
    def post(self, request):
        data = request.data
        print(data)
        information = utils.get_standard_entity_data(data)
        return Response(information)


class GetMaterial(APIView):
    def post(self, request):
        data = request.data
        print(data)
        information = utils.get_standard_entity_data(data)
        return Response(information)


class GetGenre(APIView):
    def post(self, request):
        data = request.data
        print(data)
        information = utils.get_standard_entity_data(data)
        return Response(information)
