from rest_framework import serializers

from race.serializers import RaceBaseSerializer, RaceFullSerializer
from common.util.utils import base_stat_mod_calculation, get_character_attributes, fetch_race_object_by_name_or_uuid
from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    attributes = serializers.SerializerMethodField(read_only=True)
    saving_throws = serializers.SerializerMethodField(read_only=True)
    race = RaceBaseSerializer(many=False, read_only=True)

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
        race_serializer = RaceFullSerializer(obj.race)
        attributes = {}
        if race_serializer:
            attributes = get_character_attributes(obj, race_serializer.data['racial_ability_score_increase'])
        return attributes

    def get_saving_throws(self, obj: Character):
        race_serializer = RaceFullSerializer(obj.race)
        saves = {}
        if race_serializer:
            saves = get_character_attributes(obj, race_serializer.data['racial_ability_score_increase'])
            for a in saves:
                saves[a] = base_stat_mod_calculation(saves[a])
        return saves

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
    