from rest_framework import generics

from items.serializers import ItemBaseSerializer, WeaponSerializer
from items.models import Item, Weapon

# Create your views here.
class ItemsListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemBaseSerializer


class ItemDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemBaseSerializer


class WeaponsListCreateView(generics.ListCreateAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class WeaponDeatailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
    lookup_field = "item_uuid"
