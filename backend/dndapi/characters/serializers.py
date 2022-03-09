from rest_framework import serializers

from race.serializers import RaceBaseSerializer, RaceCompleteSerializer
from common.util.utils import stat_mod_calculation, get_character_attributes, fetch_race_object_by_name_or_uuid
from characters.models import Character

"""
Serializer used for creating/updating characters
"""
class CharacterBaseSerializer(serializers.ModelSerializer):
    race = serializers.SlugRelatedField(slug_field='race_uuid', read_only=True)

    class Meta:
        model = Character
        fields = [
            'character_uuid',
            'name',
            'age',
            'gender',
            'background',
            'race',
            'base_strength',
            'base_dexterity',
            'base_constitution',
            'base_intelligence',
            'base_wisdom',
            'base_charisma',
        ]

    def create(self, validated_data):
        race = fetch_race_object_by_name_or_uuid(self.initial_data)
        if race:
            validated_data['race'] = race.first()
        return super().create(validated_data)

    def update(self, instance: Character, validated_data):
        race = fetch_race_object_by_name_or_uuid(self.initial_data)
        if race:
            instance.race = race.first()
        return super().update(instance, validated_data)

"""
Serializer used to compile the entire character into a single endpoint call
used for GET on List/Details
"""
class CharacterCompiledSerializer(CharacterBaseSerializer):
    attributes = serializers.SerializerMethodField(read_only=True)
    saving_throws = serializers.SerializerMethodField(read_only=True)
    race = RaceBaseSerializer(read_only=True)
    
    class Meta:
        model = Character
        fields = [
            'character_uuid',
            'name',
            'age',
            'gender',
            'background',
            'race',
            'attributes',
            'saving_throws',
        ]

    def get_attributes(self, obj: Character):
        race_serializer = RaceCompleteSerializer(obj.race)
        attributes = {}
        if race_serializer:
            attributes = get_character_attributes(obj, race_serializer.data)
        return attributes

    def get_saving_throws(self, obj: Character):
        race_serializer = RaceCompleteSerializer(obj.race)
        saves = {}
        if race_serializer:
            saves = get_character_attributes(obj, race_serializer.data)
            for a in saves:
                saves[a] = stat_mod_calculation(saves[a])
        return saves

    