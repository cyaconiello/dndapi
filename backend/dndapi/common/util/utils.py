import random

from race.models import Race

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
Saving Throws
"""


def base_stat_mod_calculation(base_stat: int) -> int:
    start_range = 0
    range_increase = 2
    starting_mod = -5
    return base_stat_mod_helper(base_stat, start_range, range_increase, starting_mod)


def base_stat_mod_helper(
    base_stat: int, start_range: int, range_increase: int, starting_mod: int
) -> int:
    if base_stat in range(start_range, range_increase):
        return starting_mod
    else:
        return base_stat_mod_helper(
            base_stat, start_range + 2, range_increase + 2, starting_mod + 1
        )


"""
Character attributes
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
            pass
    return race

def get_character_attributes(character, race: Race) -> (dict[str, int]):
    data = {
        "strength": int(character.base_strength),
        "dexterity": int(character.base_dexterity),
        "constitution": int(character.base_constitution),
        "intelligence": int(character.base_intelligence),
        "wisdom": int(character.base_wisdom),
        "charisma": int(character.base_charisma),
    }
    if race:
        data = {
            "strength": int(character.base_strength) + race['strength'],
            "dexterity": int(character.base_dexterity) + race['dexterity'],
            "constitution": int(character.base_constitution) + race['constitution'],
            "intelligence": int(character.base_intelligence) + race['intellegince'],
            "wisdom": int(character.base_wisdom) + race['wisdom'],
            "charisma": int(character.base_charisma) + race['charisma'],
        }
    return data
