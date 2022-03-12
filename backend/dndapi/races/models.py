import uuid
from django.db import models
from multiselectfield import MultiSelectField

from common.util.choices import size_choices, language_choices


class Race(models.Model):
    """
    Race informantion
    """

    race_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=10, choices=size_choices, default="medium")
    speed = models.PositiveIntegerField(default=30)
    # item_proficiencies =

    strength_ability_increase = models.PositiveIntegerField(default=0)
    dexterity_ability_increase = models.PositiveIntegerField(default=0)
    constitution_ability_increase = models.PositiveIntegerField(default=0)
    intelligince_ability_increase = models.PositiveIntegerField(default=0)
    wisdom_ability_increase = models.PositiveIntegerField(default=0)
    charisma_ability_increase = models.PositiveIntegerField(default=0)

    languages = MultiSelectField(choices=language_choices, null=True, blank=True)

    # class features
    # hit_die = models.CharField(max_length=6, choices=dices_choices, default='d6')

    def __str__(self):
        return self.name
