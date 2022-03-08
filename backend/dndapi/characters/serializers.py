from rest_framework import serializers

from common.util.utils import base_stat_mod_calculation, get_character_attributes
from race.models import Race
from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    race_attributes = serializers.SerializerMethodField(read_only=True)
    attributes = serializers.SerializerMethodField(read_only=True)
    saving_throws = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Character
        fields = [
            "character_uuid",
            "race_attributes",
            "name",
            "age",
            "gender",
            "background",
            "attributes",
            "saving_throws",
        ]

    def get_race_attributes(self, obj: Character):
        race: Race = Race.objects.all().filter(name=obj.race).first()
        data = {}
        if race:
            data = {
                "name": race.name,
                "uuid": race.race_uuid,
                "size": race.size,
                "speed": race.speed,
            }
        return data

    def get_attributes(self, obj: Character):
        race: Race = Race.objects.all().filter(name=obj.race).first()
        attributes = {}
        if race:
            attributes = get_character_attributes(obj, race)
        return attributes

    def get_saving_throws(self, obj: Character):
        race: Race = Race.objects.all().filter(name=obj.race).first()
        saves = {}
        if race:
            saves = get_character_attributes(obj, race)
            for a in saves:
                saves[a] = base_stat_mod_calculation(saves[a])
        return saves
