from random import randint
import uuid
from django.db import models
from multiselectfield import MultiSelectField

from common.util.choices import dices_choices,attribute_proficiencies_choicies


# Create your models here.
class CharacterClass(models.Model):
    character_class_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    hit_die = models.CharField(max_length=3, choices=dices_choices, default=dices_choices[2][0])
    primary_abilities = MultiSelectField(choices=attribute_proficiencies_choicies, null=True, blank=True, max_choices=2)
    saving_thow_proficiencies = MultiSelectField(choices=attribute_proficiencies_choicies, null=True, blank=True, max_choices=2)
    
    def __str__(self) -> str:
        return self.name