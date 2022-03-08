from rest_framework import generics

from race.serializers import RaceFullSerializer
from race.models import Race


class RaceListCreateView(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceFullSerializer
    # add bas attribute bonus


class RaceDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceFullSerializer
    lookup_field = "race_uuid"
