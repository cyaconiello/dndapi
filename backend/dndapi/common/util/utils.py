from rest_framework import fields
import random

from races.models import Race

"""
Dice Rolling
"""
def roll_dice(number_of_dice: int, number_of_sides: int) -> list[int]:
    i = 0
    list_of_rolls = []
    while i < number_of_dice:
        list_of_rolls.append(random.randint(1, number_of_sides))
        i += 1
    return list_of_rolls


def drop_dice(
    list_of_rolls: list[int], number_of_sides: int, number_to_drop: int
) -> int:
    total = 0
    number_of_rolls = list_of_rolls.__len__()
    list_of_rolls.sort()
    list_of_rolls = list_of_rolls[number_to_drop:]
    total = sum(list_of_rolls)
    if total < 10:
        roll_dice(number_of_rolls, number_of_sides)
    return total


"""
Calculation for attribute mods
Todo: add prof bonus (comes from first class)
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
def get_character_attributes(character, race: Race) -> (dict[str, int]):
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
