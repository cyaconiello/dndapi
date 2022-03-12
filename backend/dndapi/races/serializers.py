from rest_framework import serializers

from common.util.utils import CustomMultipleChoiceField
from common.util.choices import language_choices
from races.models import Race


class RaceBaseSerializer(serializers.ModelSerializer):
    languages = CustomMultipleChoiceField(choices=language_choices, required=False)

    class Meta:
        model = Race
        fields = [
            "race_uuid",
            "name",
            "size",
            "speed",
            "languages",
        ]


class RaceCompleteSerializer(RaceBaseSerializer):
    class Meta(RaceBaseSerializer.Meta):
        model = Race
        fields = RaceBaseSerializer.Meta.fields + [
            "strength_ability_increase",
            "dexterity_ability_increase",
            "constitution_ability_increase",
            "intelligince_ability_increase",
            "wisdom_ability_increase",
            "charisma_ability_increase",
            "additional_ability_increases",
        ]
