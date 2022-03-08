from rest_framework import generics

from race.models import Race
from race.serializers import RaceBaseSerializer
from characters.serializers import CharacterSerializer
from characters.models import Character


class CharactersListCreateView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = "character_uuid"
