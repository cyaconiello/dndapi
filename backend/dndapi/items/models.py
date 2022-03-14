import uuid
from django.db import models
from multiselectfield import MultiSelectField

from common.util.choices import (
    treasure_grade_choices,
    treasure_type_choices,
    currency_denomination_choices,
    dices_choices,
    damage_type_choices,
    weapon_type_choices,
    weapon_properties_choices,
)

# Create your models here.
class Item(models.Model):
    item_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    treasure_grade = models.CharField(
        max_length=120, choices=treasure_grade_choices, default="normal"
    )
    treasure_type = models.CharField(
        max_length=120, choices=treasure_type_choices, default="common"
    )
    cost = models.IntegerField(blank=True, null=True)
    currency_denomination = models.CharField(
        max_length=120, choices=currency_denomination_choices, default="gold"
    )
    weight = models.PositiveIntegerField(default=1, blank=True)

    def __str__(self) -> str:
        return self.name


class Weapon(Item):
    is_ranged = models.BooleanField(default=False)
    damage_die = models.CharField(max_length=100, choices=dices_choices, default="d6")
    number_of_die = models.PositiveIntegerField(default=1)
    damage_type = MultiSelectField(choices=damage_type_choices, null=True, blank=True)
    weapon_type = models.CharField(
        max_length=100, choices=weapon_type_choices, default="simple"
    )
    weapon_properties = MultiSelectField(
        choices=weapon_properties_choices, null=True, blank=True
    )
    min_range = models.IntegerField(blank=True, null=True)
    max_range = models.IntegerField(blank=True, null=True)
