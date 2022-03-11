from django.urls import path

from races.views import RaceDeatailsRetrieveUpdateDestroyView, RaceListCreateView
# , RaceListView, RaceDeleteView

urlpatterns = [
    path("", RaceListCreateView.as_view()),
    path("<uuid:race_uuid>/", RaceDeatailsRetrieveUpdateDestroyView.as_view()),
    # path("bulk-create/", RaceListView.as_view()),
    # path("bulk-delete/", RaceDeleteView.as_view()),
]
