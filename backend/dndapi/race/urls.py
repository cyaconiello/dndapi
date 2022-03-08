from django.urls import path

from race.views import RaceDeatailsRetrieveUpdateDestroyView, RaceListCreateView

urlpatterns = [
    path("", RaceListCreateView.as_view()),
    path("<uuid:race_uuid>/", RaceDeatailsRetrieveUpdateDestroyView.as_view()),
]
