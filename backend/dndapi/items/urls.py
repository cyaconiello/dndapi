from django.urls import path

from items.views import (
    ItemsListCreateView,
    ItemDeatailsRetrieveUpdateDestroyView,
    WeaponDeatailsRetrieveUpdateDestroyView,
    WeaponsListCreateView,
)

urlpatterns = [
    path("", ItemsListCreateView.as_view()),
    path("<uuid:item_uuid>/", ItemDeatailsRetrieveUpdateDestroyView.as_view()),
    path("weapons/", WeaponsListCreateView.as_view()),
    path(
        "weapons/<uuid:item_uuid>/", WeaponDeatailsRetrieveUpdateDestroyView.as_view()
    ),
]
