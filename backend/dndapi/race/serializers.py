from rest_framework import serializers
from languages.models import Language

from languages.serializers import LanguageSerializer
from common.util.utils import fetch_language_object_by_name_or_uuid
from race.models import Race

"""
Serializer used for returning the entire character
"""
class RaceBaseSerializer(serializers.ModelSerializer):
    languages = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Race
        fields = [
            'race_uuid',
            'name',
            'size',
            'speed',
            'languages',
        ]
    
    def get_languages(self, obj: Race):
        languages = []
        for lang in Race.objects.filter(race_uuid=obj.race_uuid).first().language_uuids.all():
            languages.append(lang.name)
        return languages
    
    def create(self, validated_data):
        languages = fetch_language_object_by_name_or_uuid(self.initial_data)
        validated_data.language_uuids.set(languages)
        return super().create(validated_data)

    def update(self, instance: Race, validated_data):
        languages = fetch_language_object_by_name_or_uuid(self.initial_data)
        instance.language_uuids.set(languages)
        return super().update(instance, validated_data)

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