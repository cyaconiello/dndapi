import uuid
from django.db import models

from race.models import Race
from common.util.utils import roll_dice, drop_dice
from common.util.choices import genders_choices


class Character(models.Model):
    """
    Character information
    """

    character_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField(default=1)
    gender = models.CharField(max_length=6, choices=genders_choices, default="male")
    background = models.TextField(blank=True)

    base_strength = models.PositiveIntegerField(
        editable=False, default=drop_dice(roll_dice(4, 6), 6, 1)
    )
    base_dexterity = models.PositiveIntegerField(
        editable=False, default=drop_dice(roll_dice(4, 6), 6, 1)
    )
    base_constitution = models.PositiveIntegerField(
        editable=False, default=drop_dice(roll_dice(4, 6), 6, 1)
    )
    base_intelligence = models.PositiveIntegerField(
        editable=False, default=drop_dice(roll_dice(4, 6), 6, 1)
    )
    base_wisdom = models.PositiveIntegerField(
        editable=False, default=drop_dice(roll_dice(4, 6), 6, 1)
    )
    base_charisma = models.PositiveIntegerField(
        editable=False, default=drop_dice(roll_dice(4, 6), 6, 1)
    )

    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
