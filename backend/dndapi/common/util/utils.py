from rest_framework import fields
import random

from character_classes.models import CharacterClass
from races.models import Race


def get_a_random_class_for_character():
    class_obj_count = CharacterClass.objects.all().count()
    char_class = CharacterClass.objects.all()[random.randint(0, class_obj_count - 1)]
    return char_class


def get_a_random_race_for_character() -> Race:
    race_obj_count = Race.objects.all().count()
    race = Race.objects.all()[random.randint(0, race_obj_count - 1)]
    return race


def get_character_stat_block_based_on_preference(validated_data) -> dict[str, int]:
    stat_block = create_stat_block_for_character()
    preference = validated_data["character_stat_preference"]

    stats = {
        "base_constitution": 0,
        "base_strength": 0,
        "base_dexterity": 0,
        "base_intelligence": 0,
        "base_wisdom": 0,
        "base_charisma": 0,
    }
    weighted = False
    if (
        preference == "race_weighted_perferred"
        or preference == "race_weighted_balanced"
    ):
        if preference == "race_weighted_perferred":
            weighted = True
        stats = sort_stats_by_racial_strengths(
            validated_data, stat_block, stats, weighted
        )
    elif (
        preference == "class_weighted_perferred"
        or preference == "class_weighted_balanced"
    ):
        if preference == "class_weighted_perferred":
            weighted = True
        print("generating stats by class")
        stats = sort_stats_by_class_strengths(validated_data, stat_block, stats, weighted)
        pass
    else:
        stats = random_assorted_stats(stat_block, stats)
    return stats


def random_assorted_stats(
    stat_block: list[int], stats: dict[str, int]
) -> dict[str, int]:
    for idx, stat in enumerate(stat_block):
        stats[list(stats)[idx]] = stat
    return stats


def sort_stats_by_class_strengths(
    validated_data, stat_block: list[int], stats: dict[str, int], perferred: bool
) -> dict[str, int]:
    # character class
    character_class = validated_data["character_class"]
    stat_block.sort()
    stat_block.reverse()
    # create new list by primary ability then saving throws
    complete_list = character_class.primary_abilities + list(set(character_class.saving_thow_proficiencies) - set(character_class.primary_abilities))
    # loop through the proficencies starting with primary ability then saving throws 
    for idx, prof in enumerate(complete_list):
        # giving the primary abilities higher weight so when sorting
        # and adding stats they get the highest
        stats[f'base_{prof}'] = len(complete_list) - idx
    stats = dict(sorted(stats.items(), key=lambda item: item[1], reverse=perferred))
    for idx, stat in enumerate(stat_block):
        stats[list(stats)[idx]] = stat
    return stats


def sort_stats_by_racial_strengths(
    validated_data,
    stat_block: list[int],
    stats: dict[str, int],
    perferred: bool,
) -> dict[str, int]:
    # character race
    race = validated_data["race"]
    # character class
    character_class = validated_data["character_class"]
    # human variant/half-elves get additional attribute stats that can be picked
    # here we determine if there is user input for these attributes
    other_attr_increases: list[str] = []
    if race.name.lower() == "half-elf" or race.name.lower() == "human variant":
        if "other_attribute_increases" in validated_data:
            for attr in validated_data["other_attribute_increases"]:
                if len(other_attr_increases) < race.additional_ability_increases:
                    other_attr_increases.append(attr)
                    stats[f"base_{attr}"] = 1
                    print(f"actual addition base_{attr}")

    stats["base_strength"] += race.strength_ability_increase
    stats["base_dexterity"] += race.dexterity_ability_increase
    stats["base_constitution"] += race.constitution_ability_increase
    stats["base_intelligence"] += race.intelligince_ability_increase
    stats["base_wisdom"] += race.wisdom_ability_increase
    stats["base_charisma"] += race.charisma_ability_increase

    # human variant/half-elves get additional attribute stats that can be picked
    # or if we need to randomly assign these attributes on character generation
    # default to class proficencies currently its random
    if race.name.lower() == "half-elf" or race.name.lower() == "human variant":
        number_of_additional_attrs_to_get: int = race.additional_ability_increases - len(
            other_attr_increases
        )
        if number_of_additional_attrs_to_get > 0:
            character_class_ability_list: list[str] = character_class.primary_abilities + list(set(character_class.saving_thow_proficiencies) - set(character_class.primary_abilities))
            while number_of_additional_attrs_to_get > 0:
                # get the current choices avaiable for attr increases
                # that have not already been increased
                choices = [stat for stat in stats if stats[stat] == 0]
                if len(character_class_ability_list)-1 >= number_of_additional_attrs_to_get:
                    # check that against the list of class proficencies that
                    # have not been increased yet
                    character_class_ability_list = [ability for ability in character_class_ability_list if f'base_{ability}' in choices]
                    # pare that list down by the number of stat increases needed
                    character_class_ability_list = character_class_ability_list[:number_of_additional_attrs_to_get]
                if len(character_class_ability_list) > 0:
                    # add via class proficencies
                    attr_to_increase = f'base_{character_class_ability_list[0]}'    
                else:
                    # random available stat increase
                    attr_to_increase = choices[random.randint(0, len(choices) - 1)]
                other_attr_increases.append(attr_to_increase.replace("base_", ""))
                stats[attr_to_increase] += 1
                number_of_additional_attrs_to_get += -1

    stat_block.sort()
    stat_block.reverse()
    stats = dict(sorted(stats.items(), key=lambda item: item[1], reverse=perferred))
    for idx, stat in enumerate(stat_block):
        stats[list(stats)[idx]] = stat
    return stats


def create_stat_block_for_character(player_character=True) -> list[int]:
    attribute_rolls = []
    while len(attribute_rolls) < 6:
        attribute_rolls.append(drop_dice(roll_dice(4, 6), 4, 6, 1, player_character))
    return attribute_rolls


def roll_dice(number_of_dice: int, number_of_sides: int) -> list[int]:
    i = 0
    list_of_rolls = []
    if number_of_dice:
        while i < number_of_dice:
            list_of_rolls.append(random.randint(1, number_of_sides))
            i += 1
    return list_of_rolls


def drop_dice(
    list_of_rolls: list[int],
    number_of_dice: int,
    number_of_sides: int,
    number_to_drop: int,
    player_character: bool = True,
) -> int:
    total = 0
    if list_of_rolls:
        list_of_rolls.sort()
        list_of_rolls = list_of_rolls[number_to_drop:]
        total = sum(list_of_rolls)
        if player_character and total < 10:
            return drop_dice(roll_dice(number_of_dice, number_of_sides), 4, 6, 1)
    return total


def stat_mod_calculation(
    base_stat: int, proficiency_bonus: int = 0, proficient: bool = False
) -> int:
    start_range = 0
    range_increase = 2
    starting_mod = -5
    if proficient:
        base_stat += proficiency_bonus
    return stat_mod_helper(base_stat, start_range, range_increase, starting_mod)


def stat_mod_helper(
    base_stat: int, start_range: int, range_increase: int, starting_mod: int
) -> int:
    if base_stat in range(start_range, range_increase):
        return starting_mod
    else:
        return stat_mod_helper(
            base_stat, start_range + 2, range_increase + 2, starting_mod + 1
        )

def fetch_class_object_by_name_or_uuid(request) -> CharacterClass:
    character_class = None
    if "character_class" in request:
        if "uuid" in request["character_class"]:
            character_class = CharacterClass.objects.filter(character_class_uuid=request["character_class"]["uuid"])
        if not character_class and "name" in request["character_class"]:
            character_class = CharacterClass.objects.filter(name__iexact=request["character_class"]["name"])
    return character_class

def fetch_race_object_by_name_or_uuid(request) -> Race:
    race = None
    if "race" in request:
        if "uuid" in request["race"]:
            race = Race.objects.filter(race_uuid=request["race"]["uuid"])
        if not race and "name" in request["race"]:
            race = Race.objects.filter(name__iexact=request["race"]["name"])
    return race


def get_character_attributes(character, race: Race) -> dict[str, int]:
    data = {
        "strength": int(character.base_strength)
        + int(race["strength_ability_increase"]),
        "dexterity": int(character.base_dexterity)
        + int(race["dexterity_ability_increase"]),
        "constitution": int(character.base_constitution)
        + int(race["constitution_ability_increase"]),
        "intelligence": int(character.base_intelligence)
        + int(race["intelligince_ability_increase"]),
        "wisdom": int(character.base_wisdom) + int(race["wisdom_ability_increase"]),
        "charisma": int(character.base_charisma)
        + int(race["charisma_ability_increase"]),
    }
    return data


class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))
