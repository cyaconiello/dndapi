from rest_framework import serializers

from common.util.utils import CustomMultipleChoiceField
from common.util.choices import language_choices
from races.models import Race

"""
Serializer used for returning the entire character
"""
class RaceBaseSerializer(serializers.ModelSerializer):
    languages = CustomMultipleChoiceField(choices=language_choices, required=False)
    class Meta:
        model = Race
        fields = [
            'race_uuid',
            'name',
            'size',
            'speed',
            'languages',
        ]

"""
Serializer used for GET/PUT/POST for Races
"""
class RaceCompleteSerializer(RaceBaseSerializer):
    class Meta(RaceBaseSerializer.Meta):
        model = Race
        fields = RaceBaseSerializer.Meta.fields +  [
            'strength_ability_increase',
            'dexterity_ability_increase',
            'constitution_ability_increase',
            'intelligince_ability_increase',
            'wisdom_ability_increase',
            'charisma_ability_increase',
        ]
# """
# Serializer used for bulk creation of Races
# """
# class RaceBulkCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Race
#         exclude = ['name']
    