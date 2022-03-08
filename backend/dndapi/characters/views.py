from rest_framework import generics
from race.models import Race

from characters.serializers import CharacterSerializer
from characters.models import Character


class CharactersListCreateView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = "character_uuid"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if "race_attributes" in request.data:
            updated_race = {}
            if "uuid" in request.data["race_attributes"]:
                updated_race = Race.objects.filter(
                    race_uuid=request.data["race_attributes"]["uuid"]
                )
            if not updated_race and "name" in request.data["race_attributes"]:
                updated_race = Race.objects.filter(
                    name__iexact=request.data["race_attributes"]["name"]
                )
            if updated_race:
                instance.race = updated_race.first()
                instance.save()
        return super().update(request, *args, **kwargs)
