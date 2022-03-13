from rest_framework import serializers

from common.util.utils import CustomMultipleChoiceField
from common.util.choices import attribute_proficiencies_choicies
from character_classes.models import CharacterClass


class CharacterClassBaseSerializer(serializers.ModelSerializer):
    primary_abilities = CustomMultipleChoiceField(choices=attribute_proficiencies_choicies, required=False)
    saving_thow_proficiencies = CustomMultipleChoiceField(choices=attribute_proficiencies_choicies, required=False)

    class Meta:
        model = CharacterClass
        fields = [
            "character_class_uuid",
            "name",
            "description",
            "hit_die",
            "primary_abilities",
            "saving_thow_proficiencies",   
        ]


class CharacterClassCompleteSerializer(CharacterClassBaseSerializer):
    class Meta(CharacterClassBaseSerializer.Meta):
        model = CharacterClass
        fields = CharacterClassBaseSerializer.Meta.fields + []
