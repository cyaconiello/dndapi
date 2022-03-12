import uuid
from django.db import models
from multiselectfield import MultiSelectField

from common.util.choices import (
    size_choices,
    language_choices,
)


class Race(models.Model):
    race_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    size = models.CharField(
        max_length=10, choices=size_choices, default=size_choices[2][0]
    )
    speed = models.PositiveIntegerField(default=30)

    strength_ability_increase = models.PositiveIntegerField(default=0)
    dexterity_ability_increase = models.PositiveIntegerField(default=0)
    constitution_ability_increase = models.PositiveIntegerField(default=0)
    intelligince_ability_increase = models.PositiveIntegerField(default=0)
    wisdom_ability_increase = models.PositiveIntegerField(default=0)
    charisma_ability_increase = models.PositiveIntegerField(default=0)
    additional_ability_increases = models.PositiveIntegerField(
        help_text="For every additional +1 to stat attribute increase this value by 1. (example: Half Elf gets 2 addional stat increase by 1, so this value would be 2.)",
        default=0,
    )

    languages = MultiSelectField(choices=language_choices, null=True, blank=True)

    def __str__(self):
        return self.name
