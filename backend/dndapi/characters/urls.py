from django.urls import path

from characters.views import (
    CharacterDeatailsRetrieveUpdateDestroyView,
    CharactersListCreateView,
)

urlpatterns = [
    path("", CharactersListCreateView.as_view()),
    path(
        "<uuid:character_uuid>/", CharacterDeatailsRetrieveUpdateDestroyView.as_view()
    ),
]
