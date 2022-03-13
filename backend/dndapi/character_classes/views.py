from rest_framework import generics

from character_classes.serializers import (
    CharacterClassBaseSerializer,
    CharacterClassCompleteSerializer,
)
from character_classes.models import CharacterClass


class CharacterClassListCreateView(generics.ListCreateAPIView):
    queryset = CharacterClass.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CharacterClassBaseSerializer
        return CharacterClassCompleteSerializer


class CharacterClassDeatailsRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = CharacterClass.objects.all()
    lookup_field = "character_class_uuid"

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return CharacterClassBaseSerializer
        return CharacterClassCompleteSerializer
