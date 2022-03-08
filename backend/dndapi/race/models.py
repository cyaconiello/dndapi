import uuid
from django.db import models

from common.util.choices import size_choices


class Race(models.Model):
    """
    Race informantion
    """

    race_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, default="Dwarf")
    description = models.TextField(blank=True)
    size = models.CharField(max_length=10, choices=size_choices, default="medium")
    speed = models.PositiveIntegerField(default=30)

    strength_ability_increase = models.PositiveIntegerField(default=0)
    dexterity_ability_increase = models.PositiveIntegerField(default=0)
    constitution_ability_increase = models.PositiveIntegerField(default=0)
    intellegince_ability_increase = models.PositiveIntegerField(default=0)
    wisdom_ability_increase = models.PositiveIntegerField(default=0)
    charisma_ability_increase = models.PositiveIntegerField(default=0)

    # class features
    # hit_die = models.CharField(max_length=6, choices=dices_choices, default='d6')
    # attribute_proficiencies = MultipleChoiceField(choices=attribute_proficiencies_choicies)

    def __str__(self):
        return self.name
