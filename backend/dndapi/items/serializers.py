from rest_framework import serializers

from items.models import Item, Weapon
from common.util.utils import CustomMultipleChoiceField
from common.util.choices import damage_type_choices, weapon_properties_choices

"""
Serializer used for returning the items
"""


class ItemBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "item_uuid",
            "name",
            "description",
            "treasure_grade",
            "treasure_type",
            "cost",
            "currency_denomination",
            "weight",
        ]


"""
Serializer used for returning the Weapons
"""


class WeaponSerializer(ItemBaseSerializer, serializers.HyperlinkedModelSerializer):
    damage_type = CustomMultipleChoiceField(choices=damage_type_choices, required=False)
    weapon_properties = CustomMultipleChoiceField(
        choices=weapon_properties_choices, required=False
    )

    class Meta(ItemBaseSerializer.Meta):
        model = Weapon
        fields = ItemBaseSerializer.Meta.fields + [
            "damage_die",
            "number_of_die",
            "damage_type",
            "is_ranged",
            "weapon_type",
            "weapon_properties",
            "min_range",
            "max_range",
        ]
