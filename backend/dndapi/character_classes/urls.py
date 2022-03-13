from django.urls import path

from character_classes.views import (
    CharacterClassListCreateView,
    CharacterClassDeatailsRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("", CharacterClassListCreateView.as_view()),
    path(
        "<uuid:character_class_uuid>/",
        CharacterClassDeatailsRetrieveUpdateDestroyView.as_view(),
    ),
]
