from django.urls import path

from .views import ArtworkList


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('artworks/', ArtworkList.as_view()),
]
