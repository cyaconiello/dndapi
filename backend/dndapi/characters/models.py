import uuid
from django.db import models

from races.models import Race
from common.util.utils import roll_dice, drop_dice
from common.util.choices import genders_choices


class Character(models.Model):
    """
    Character information
    """
    print('Character model loading')
    character_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField(default=1)
    gender = models.CharField(max_length=6, choices=genders_choices, default="male")
    background = models.TextField(blank=True)

    base_strength = models.PositiveIntegerField(editable=False, default=0)
    base_dexterity = models.PositiveIntegerField(editable=False, default=0)
    base_constitution = models.PositiveIntegerField(editable=False, default=0)
    base_intelligence = models.PositiveIntegerField(editable=False, default=0)
    base_wisdom = models.PositiveIntegerField(editable=False, default=0)
    base_charisma = models.PositiveIntegerField(editable=False, default=0)

    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
