from rest_framework import fields
import random

from races.models import Race

"""
Dice Rolling
"""
"""
Sort stats based on racial ability mod
"""
def sort_stats_by_racial_strengths(race, stat_block):
    race = race.first()
    data = {
        "base_strength": int(race.strength_ability_increase),
        "base_dexterity": int(race.dexterity_ability_increase),
        "base_constitution": int(race.constitution_ability_increase),
        "base_intelligence": int(race.intelligince_ability_increase),
        "base_wisdom": int(race.wisdom_ability_increase),
        "base_charisma": int(race.charisma_ability_increase),
    }
    data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    for idx, stat in enumerate(stat_block):
        data[list(data)[idx]] = stat
    return data
"""
create stat block for characters/NPCs
"""
def create_stat_block_for_character(player_character=True):
    attribute_rolls = []
    while len(attribute_rolls) < 6:
        attribute_rolls.append(drop_dice(roll_dice(4, 6), 4, 6, 1, player_character))
    attribute_rolls.sort()
    attribute_rolls.reverse()
    return attribute_rolls
"""
Roll dice by number of dice and how many sides
"""
def roll_dice(number_of_dice: int, number_of_sides: int) -> list[int]:
    i = 0
    list_of_rolls = []
    if number_of_dice:
        while i < number_of_dice:
            list_of_rolls.append(random.randint(1, number_of_sides))
            i += 1
    return list_of_rolls
"""
Player character drop dice function and home brew stats greater than 9
"""
def drop_dice(
    list_of_rolls: list[int],
    number_of_dice: int,
    number_of_sides: int,
    number_to_drop: int,
    player_character: bool = True
) -> int:
    total = 0
    if list_of_rolls:
        list_of_rolls.sort()
        list_of_rolls = list_of_rolls[number_to_drop:]
        total = sum(list_of_rolls)
        if player_character and total < 10:
            return drop_dice(roll_dice(number_of_dice, number_of_sides), 4, 6, 1)
    return total


"""
Calculation for attribute mods
"""
def stat_mod_calculation(base_stat: int, proficiency_bonus: int = 0, proficient: bool = False) -> int:
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

"""
Getting the Race from user request obj by 'uuid' or 'name'
"""
def fetch_race_object_by_name_or_uuid(request):
    race = {}
    if "race" in request:
        if "uuid" in request["race"]:
            race = Race.objects.filter(
                race_uuid=request["race"]["uuid"]
            )
        if not race and "name" in request["race"]:
            race = Race.objects.filter(
                name__iexact=request["race"]["name"]
            )
    return race

"""
Formatting the Character attributes:
since you cant have a character without a race no condition needed
"""
def get_character_attributes(character, race) -> (dict[str, int]):
    data = {
        "strength": int(character.base_strength) + int(race['strength_ability_increase']),
        "dexterity": int(character.base_dexterity) + int(race['dexterity_ability_increase']),
        "constitution": int(character.base_constitution) + int(race['constitution_ability_increase']),
        "intelligence": int(character.base_intelligence) + int(race['intelligince_ability_increase']),
        "wisdom": int(character.base_wisdom) + int(race['wisdom_ability_increase']),
        "charisma": int(character.base_charisma) + int(race['charisma_ability_increase']),
    }
    return data


class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))
