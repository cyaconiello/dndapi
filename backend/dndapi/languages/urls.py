from django.urls import path

from languages.views import LanguagesListCreateView, LanguagesRetrieveUpdateDestroyView

urlpatterns = [
    path("", LanguagesListCreateView.as_view()),
    path("<uuid:language_uuid>/", LanguagesRetrieveUpdateDestroyView.as_view()),
]
