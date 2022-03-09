from rest_framework import serializers

from race.models import Race

"""
Serializer used for returning the entire character
"""
class RaceBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = [
            'race_uuid',
            'name',
            'size',
            'speed',
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
            'intellegince_ability_increase',
            'wisdom_ability_increase',
            'charisma_ability_increase',
        ]