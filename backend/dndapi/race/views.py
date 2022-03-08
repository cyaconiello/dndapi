from rest_framework import generics

from race.serializers import RaceSerializer
from race.models import Race


class RaceListCreateView(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    # add bas attribute bonus


class RaceDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    lookup_field = "race_uuid"
