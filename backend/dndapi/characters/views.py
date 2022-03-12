from rest_framework import generics

from characters.serializers import CharacterBaseSerializer, CharacterCompiledSerializer
from characters.models import Character


class CharactersListCreateView(generics.ListCreateAPIView):
    queryset = Character.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CharacterBaseSerializer
        return CharacterCompiledSerializer


class CharacterDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    lookup_field = "character_uuid"

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return CharacterBaseSerializer
        return CharacterCompiledSerializer
