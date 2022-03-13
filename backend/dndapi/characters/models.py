from random import randint
import uuid
from django.db import models
from multiselectfield import MultiSelectField

from character_classes.models import CharacterClass
from races.models import Race
from common.util.choices import (
    genders_choices,
    attribute_proficiencies_choicies,
    character_generation_stat_preference_choices,
)


class Character(models.Model):
    character_stat_preference = models.CharField(
        max_length=24,
        choices=character_generation_stat_preference_choices,
        default=character_generation_stat_preference_choices[0][0],
    )
    other_attribute_increases = MultiSelectField(
        choices=attribute_proficiencies_choicies, blank=True, null=True, max_choices=2
    )

    character_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    # TODO: refactor to sync with race or to roll for it
    age = models.PositiveIntegerField(default=randint(10, 30))
    gender = models.CharField(
        max_length=6, choices=genders_choices, default=genders_choices[randint(0, 1)][0]
    )
    background = models.TextField(blank=True)
    level = models.PositiveIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)
    max_hp = models.PositiveIntegerField(default=0)
    
    base_strength = models.PositiveIntegerField(editable=False, default=0)
    base_dexterity = models.PositiveIntegerField(editable=False, default=0)
    base_constitution = models.PositiveIntegerField(editable=False, default=0)
    base_intelligence = models.PositiveIntegerField(editable=False, default=0)
    base_wisdom = models.PositiveIntegerField(editable=False, default=0)
    base_charisma = models.PositiveIntegerField(editable=False, default=0)

    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
