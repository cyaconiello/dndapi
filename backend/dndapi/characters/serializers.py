from rest_framework import serializers

from common.util.utils import (
    CustomMultipleChoiceField,
    stat_mod_calculation,
    get_character_attributes,
    fetch_race_object_by_name_or_uuid,
    get_character_stat_block_based_on_preference,
    get_a_random_race_for_character,
    # get_a_random_class_for_character,
)
from common.util.choices import attribute_proficiencies_choicies
from races.serializers import RaceBaseSerializer, RaceCompleteSerializer
from character_classes.serializers import CharacterClassBaseSerializer
from characters.models import Character


class CharacterBaseSerializer(serializers.ModelSerializer):
    race = serializers.SlugRelatedField(slug_field="race_uuid", read_only=True)
    character_class = serializers.SlugRelatedField(slug_field="character_class_uuid", read_only=True)
    other_attribute_increases = CustomMultipleChoiceField(
        choices=attribute_proficiencies_choicies, required=False
    )

    # Character.objects.all().delete()
    class Meta:
        model = Character
        fields = [
            "character_uuid",
            "name",
            "age",
            "gender",
            "background",
            "level",
            "experience",
            "max_hp",
            "race",
            "character_class",
            "character_stat_preference",
            "other_attribute_increases",
            "base_strength",
            "base_dexterity",
            "base_constitution",
            "base_intelligence",
            "base_wisdom",
            "base_charisma",
        ]

    def create(self, validated_data):
        # get race from user input
        race = fetch_race_object_by_name_or_uuid(self.initial_data)
        # TODO: get class for character
        char_class = None
        # if there is no race provided get a random race
        if not race:
            validated_data["race"] = get_a_random_race_for_character()
        else:
            validated_data["race"] = race.first()
        # if there is no class provided get a random class
        if not char_class:
            # validated_data["class"] = get_a_random_class_for_character()
            pass
        else:
            # validated_data["class"] = char_class.first()
            pass
        # TODO:
        # throw validation error if you pass more than 2 other attributes
        # or non unique or if the race doesnt has self picked attributes
        if (
            validated_data["race"].name.lower() == "half-elf"
            or validated_data["race"].name.lower() == "human variant"
        ):
            validated_data["other_attribute_increases"] = list(
                validated_data["other_attribute_increases"]
            )[:2]
        else:
            validated_data["other_attribute_increases"] = []
        # save the character to creat an instance
        instance = super().create(validated_data)
        # get the stats based on race/class/prefernce
        stats = get_character_stat_block_based_on_preference(validated_data)
        # update the instance stats
        instance.base_strength = stats["base_strength"]
        instance.base_dexterity = stats["base_dexterity"]
        instance.base_constitution = stats["base_constitution"]
        instance.base_wisdom = stats["base_wisdom"]
        instance.base_intelligence = stats["base_intelligence"]
        instance.base_charisma = stats["base_charisma"]
        # resave the instance
        instance.save()
        return instance

    def update(self, instance: Character, validated_data):
        # TODO: disallow updating the race
        race = fetch_race_object_by_name_or_uuid(self.initial_data)
        if race:
            instance.race = race.first()
        # TODO: multiclass?
        return super().update(instance, validated_data)


class CharacterCompiledSerializer(CharacterBaseSerializer):
    attributes = serializers.SerializerMethodField(read_only=True)
    saving_throws = serializers.SerializerMethodField(read_only=True)
    race = RaceBaseSerializer(read_only=True)
    character_class = CharacterClassBaseSerializer(read_only=True)

    class Meta:
        model = Character
        read_only_fields = ("bar",)
        fields = [
            "character_uuid",
            "name",
            "age",
            "gender",
            "level",
            "experience",
            "max_hp",
            "background",
            "race",
            "character_class",
            "attributes",
            "saving_throws",
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
