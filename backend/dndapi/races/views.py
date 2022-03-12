from rest_framework import generics

from races.serializers import RaceCompleteSerializer
from races.models import Race


class RaceListCreateView(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceCompleteSerializer


class RaceDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceCompleteSerializer
    lookup_field = "race_uuid"
