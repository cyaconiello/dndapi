from rest_framework import generics

# from common.util.batch_create import fetch_from_json
from races.serializers import RaceCompleteSerializer

# RaceBulkCreateSerializer
from races.models import Race


class RaceListCreateView(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceCompleteSerializer


class RaceDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceCompleteSerializer
    lookup_field = "race_uuid"


# class RaceListView(generics.ListAPIView):
#     queryset = Race.objects.all()

#     def get_serializer_class(self):
#         if not Race.objects.all():
#             json_races = fetch_from_json('races')
#             for r in json_races:
#                 race = RaceCompleteSerializer(data=r, many=True)
#                 if race.is_valid():
#                     race.save()
#         return RaceCompleteSerializer

# class RaceDeleteView(generics.ListAPIView):
#     queryset = Race.objects.all()

#     def get_serializer_class(self):
#         if Race.objects.all():
#            Race.objects.all().delete()
#         return RaceCompleteSerializer
