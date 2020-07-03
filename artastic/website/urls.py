from django.urls import path

from .views import ArtworkList, GetArtist, GetLocation, GetMovement, GetMaterial, GetGenre, ArtworkByQ


app_name = "articles"

# app_name will help us do a reverse look-up latter.
# ACHTUNG! NEUE URLS WERDEN IMMER NACH DEM OBJECTTYPE ANGELEGT ALSO PERSON, ARTWORK, LOCATION ....
urlpatterns = [
    path('artwork/', ArtworkList.as_view()),
    path('person/', GetArtist.as_view()),
    path('location/', GetLocation.as_view()),
    path('movement/', GetMovement.as_view()),
    path('material/', GetMaterial.as_view()),
    path('genre/', GetGenre.as_view()),
    path('artworkByQ/', ArtworkByQ.as_view()),

]
