from rest_framework import generics
from race.models import Race

from characters.serializers import CharacterSerializer
from characters.models import Character


class CharactersListCreateView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def perform_create (self, serializer: CharacterSerializer):
        race = fetch_race_object(self.request)
        print()
        if race:
            serializer.save(race=race.first())
        return super().perform_create(serializer)


class CharacterDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = "character_uuid"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        race = fetch_race_object(request)
        if race:
            instance.race = race.first()
            instance.save()
        return super().update(request, *args, **kwargs)

# put in utility file?
def fetch_race_object(request):
    race = {}
    if "race_attributes" in request.data:
        if "uuid" in request.data["race_attributes"]:
            race = Race.objects.filter(
                race_uuid=request.data["race_attributes"]["uuid"]
            )
        if not race and "name" in request.data["race_attributes"]:
            race = Race.objects.filter(
                name__iexact=request.data["race_attributes"]["name"]
            )
    return race