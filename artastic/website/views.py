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
        informations = utils.get_all(data['data'])
        return Response(informations)
