from rest_framework import fields
import random

from races.models import Race


def get_a_random_class_for_character():
    return None


def get_a_random_race_for_character() -> Race:
    # totally rand race
    race_obj_count = Race.objects.all().count()
    race = Race.objects.all()[random.randint(0, race_obj_count - 1)]
    return race


def get_character_stat_block_based_on_preference(
    race: Race, character_class, stat_block: list[int], preference: str
) -> dict[str, int]:
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
        stats = sort_stats_by_racial_strengths(race, stat_block, stats, weighted)
    elif character_class and (
        preference == "class_weighted_perferred"
        or preference == "class_weighted_balanced"
    ):
        if preference == "class_weighted_perferred":
            weighted = True
        print("generating stats by class")
        stats = sort_stats_by_class_strengths(character_class, stat_block, weighted)
        pass
    else:
        stats = random_assorted_stats(stat_block, stats)
    print(stats)
    return stats


def random_assorted_stats(
    stat_block: list[int], stats: dict[str, int]
) -> dict[str, int]:
    for idx, stat in enumerate(stat_block):
        stats[list(stats)[idx]] = stat
    return stats


def sort_stats_by_class_strengths(
    char_class, stat_block: list[int], stats: dict[str, int], perferred: bool
) -> dict[str, int]:
    stat_block.sort()
    stat_block.reverse()
    print(stat_block)
    # TODO: once classes are made sort by proffiency
    # stats['base_strength'] = int(race.strength_ability_increase),
    # stats['base_dexterity'] = int(race.dexterity_ability_increase),
    # stats['base_constitution'] = int(race.constitution_ability_increase),
    # stats['base_intelligence'] = int(race.intelligince_ability_increase),
    # stats['base_wisdom'] = int(race.wisdom_ability_increase),
    # stats['base_charisma'] = int(race.charisma_ability_increase),
    print(stat)
    stats = dict(sorted(stats.items(), key=lambda item: item[1], reverse=perferred))
    for idx, stat in enumerate(stat_block):
        stats[list(stats)[idx]] = stat
    return stats


def sort_stats_by_racial_strengths(
    race: Race, stat_block: list[int], stats: dict[str, int], perferred: bool
) -> dict[str, int]:
    stat_block.sort()
    stat_block.reverse()
    # TODO: adding in ability to increase a ability score field for
    # half elf 2x other ability score +1
    stats["base_strength"] = (int(race.strength_ability_increase),)
    stats["base_dexterity"] = (int(race.dexterity_ability_increase),)
    stats["base_constitution"] = (int(race.constitution_ability_increase),)
    stats["base_intelligence"] = (int(race.intelligince_ability_increase),)
    stats["base_wisdom"] = (int(race.wisdom_ability_increase),)
    stats["base_charisma"] = (int(race.charisma_ability_increase),)

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
