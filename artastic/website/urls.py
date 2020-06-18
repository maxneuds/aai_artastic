from django.urls import path

from .views import ArtworkList, GetArtist


app_name = "articles"

# app_name will help us do a reverse look-up latter.
# ACHTUNG! NEUE URLS WERDEN IMMER NACH DEM OBJECTTYPE ANGELEGT ALSO PERSON, ARTWORK, LOCATION ....
urlpatterns = [
    path('artwork/', ArtworkList.as_view()),
    path('person/', GetArtist.as_view())
]
