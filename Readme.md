# Endpoints
## List
 - [[GET/POST] `/characters/`](#characters)
 - [[GET/PUT/DELTE] `/characters/{character-uuid}/`](#characters-update)
 - [[GET/POST] `/races/`](#races)
 - [[GET/PUT/DELETE] `/races/{race-uuid}/`](#races-update)
 - [[GET/POST] `/classes/`](#classes)
 - [[GET/PUT/DELETE] `/classes/{class-uuid}/`](#classes-update)
 - [[GET/POST] `/items/`](#items)
 - [[GET/PUT/DELETE] `/items/{item-uuid}/`](#items-update)
 - [[GET/POST] `/items/weapons/`](#weapons))
 - [[GET/PUT/DELETE] `/items/weapons/{item-uuid}/`](#weapons-update)


<a id="characters"></a>
### [GET/POST] `/characters/`

Everything is optional but the name, for race and class one can use the name or uuid (uuid will supersede name if they dont match).
<br />

*Note: at some point name will be optional as well and will pull from a table base on race/class.*
<br />

`gender` has these choices available (defaults to `random`):
```json
[
    "male",
    "female"
]
```
<br />

`character_stat_preference` has these choices available (defaults to `random`):
```json
[
    "random",
    "race_weighted_perferred",
    "race_weighted_balanced",
    "class_weighted_perferred"
]
```
<br />

* *(Note: this is for human variant/half-elf where you can pick ability stat increases)* *
`other_attribute_increases` has these choices available (will default to class primary ability/saving throw):
```json
[
    "strength",
    "constitution",
    "dexterity",
    "intelligence",
    "wisdom",
    "carisma"
]
```
<br />

Payload Schema
```ts
{
    "name": string,
    "age": number,
    "gender": string,
    "level": number,
    "experience": number,
    "background": string,
    "character_stat_preference": string,
    "other_attribute_increases": string[],
    "race": {
        "race_uuid": uuid,
        "name": string
    },
    "character_class": {
        "character_class_uuid": uuid,
        "name": string
    }
}
```
Response scheme
```ts
[
    {
        "character_uuid": string,
        "name": string,
        "age": number,
        "gender": string,
        "level": number,
        "experience": number,
        "max_hp": numer,
        "background": string,
        "race": {
            "race_uuid": string,
            "name": string,
            "size": string,
            "speed": number,
            "languages": string[]
        },
        "character_class": {
            "character_class_uuid": string,
            "name": string,
            "description": string,
            "hit_die": string,
            "primary_abilities": string[],
            "saving_thow_proficiencies": string[]
        },
        "attributes": {
            "strength": number,
            "dexterity": number,
            "constitution": number,
            "intelligence": number,
            "wisdom": number,
            "charisma": number
        },
        "saving_throws": {
            "strength": number,
            "dexterity": number,
            "constitution": number,
            "intelligence": number,
            "wisdom": number,
            "charisma": number
        }
    }
]
```
<a id="characters-update"></a>
### [GET/PUT/DELTE] `/characters/{character-uuid}/`
Endpoint is used to fetch/update/delete a character.
*TBD: rules for updating/leveling*

<br />

Payload Schema
```ts
{
    "name": string,
    "age": number,
    "gender": string,
    "level": number,
    "experience": number,
    "background": string,
    "character_stat_preference": string,
    "other_attribute_increases": string[],
    "race": {
        "race_uuid": uuid,
        "name": string
    },
    "character_class": {
        "character_class_uuid": uuid,
        "name": string
    }
}
```
Response scheme
```ts
{
    "character_uuid": string,
    "name": string,
    "age": number,
    "gender": string,
    "level": number,
    "experience": number,
    "max_hp": numer,
    "background": string,
    "race": {
        "race_uuid": string,
        "name": string,
        "size": string,
        "speed": number,
        "languages": string[]
    },
    "character_class": {
        "character_class_uuid": string,
        "name": string,
        "description": string,
        "hit_die": string,
        "primary_abilities": string[],
        "saving_thow_proficiencies": string[]
    },
    "attributes": {
        "strength": number,
        "dexterity": number,
        "constitution": number,
        "intelligence": number,
        "wisdom": number,
        "charisma": number
    },
    "saving_throws": {
        "strength": number,
        "dexterity": number,
        "constitution": number,
        "intelligence": number,
        "wisdom": number,
        "charisma": number
    }
}
```
<a id="races"></a>
### [GET/POST] `/races/`
Endpoint is used to fetch/create a race(s).
<br />

`size` has these choices available (defaults to `medium`):
```python
(
    ("tiny", "tiny"),  # 2.5x2.5
    ("small", "small"),  # 5x5
    ("medium", "medium"),  # 5x5
    ("large", "large"),  # 10x10
    ("huge", "huge"),  # 15x15
    ("gargantuan", "gargantuan"),  # 20x20
)
```
<br />

`languages` has these choices available (defaults to `null`):
```python
(
    ("common", "common"),
    ("dwarvish", "dwarvish"),
    ("elvish", "elvish"),
    ("giant", "giant"),
    ("gnomish", "gnomish"),
    ("goblin", "goblin"),
    ("halfling", "halfling"),
    ("orc", "orc"),
    ("abyssal", "abyssal"),
    ("celestial", "celestial"),
    ("deep speech", "deep speech"),
    ("infernal", "infernal"),
    ("primordial", "primordial"),
    ("sylvan", "sylvan"),
    ("draconic", "draconic"),
    ("undercommon", "undercommon"),
)
```
<br />

`speed` (defaults to 30) <br />
`strength_ability_increase` (defaults to `0`) <br />
`dexterity_ability_increase` (defaults to `0`) <br />
`constitution_ability_increase` (defaults to `0`) <br />
`intelligince_ability_increase` (defaults to `0`) <br />
`wisdom_ability_increase` (defaults to `0`) <br />
`charisma_ability_increase` (defaults to `0`) <br />
`additional_ability_increases` (defaults to `0`) <br />

Payload Schema
```ts
{
    "name": string,
    "size": string,
    "speed": number,
    "languages": string[],
    "strength_ability_increase": number,
    "dexterity_ability_increase": number,
    "constitution_ability_increase": number,
    "intelligince_ability_increase": number,
    "wisdom_ability_increase": number,
    "charisma_ability_increase": number,
    "additional_ability_increases": number
}
```
Response scheme
```ts
[
    {
        "race_uuid": string,
        "name": string,
        "size": string,
        "speed": number,
        "languages": string[],
        "strength_ability_increase": number,
        "dexterity_ability_increase": number,
        "constitution_ability_increase": number,
        "intelligince_ability_increase": number,
        "wisdom_ability_increase": number,
        "charisma_ability_increase": number,
        "additional_ability_increases": number
    }
]
```
<a id="races-update"></a>
### [GET/PUT/DELETE] `/races/{race-uuid}/`
Endpoint is used to fetch/update/delete a race.
<br />

Payload Schema
```ts
{
    "name": string,
    "size": string,
    "speed": number,
    "languages": string[],
    "strength_ability_increase": number,
    "dexterity_ability_increase": number,
    "constitution_ability_increase": number,
    "intelligince_ability_increase": number,
    "wisdom_ability_increase": number,
    "charisma_ability_increase": number,
    "additional_ability_increases": number
}
```
Response scheme
```ts
{
    "race_uuid": string,
    "name": string,
    "size": string,
    "speed": number,
    "languages": string[],
    "strength_ability_increase": number,
    "dexterity_ability_increase": number,
    "constitution_ability_increase": number,
    "intelligince_ability_increase": number,
    "wisdom_ability_increase": number,
    "charisma_ability_increase": number,
    "additional_ability_increases": number
}
```
<a id="classes"></a>
### [GET/POST] `/classes/`
Endpoint is used to fetch/create a class(es).
<br />
`name` is again the only required field. <br />
`hit_die` has these choices available (defaults to `d8`): <br />

```python
(
    ("d4", "d4"),
    ("d6", "d6"),
    ("d8", "d8"),
    ("d10", "d10"),
    ("d12", "d12"),
    ("d20", "d20"),
)
```
`primary_abilities` has these choices available (defaults to `null` *can be a max of 2*): <br />
```python
(
    ("strength", "strength"),
    ("dexterity", "dexterity"),
    ("constitution", "constitution"),
    ("intelligence", "intelligence"),
    ("wisdom", "wisdom"),
    ("charisma", "charisma"),
)
```
`saving_thow_proficiencies` has these choices available (defaults to `null` *can be a max of 2*): <br />
```python
(
    ("strength", "strength"),
    ("dexterity", "dexterity"),
    ("constitution", "constitution"),
    ("intelligence", "intelligence"),
    ("wisdom", "wisdom"),
    ("charisma", "charisma"),
)
```

Payload Schema
```ts
{
    "name": string,
    "description": string,
    "hit_die": string,
    "primary_abilities": string[],
    "saving_thow_proficiencies": string[]
}
```
Response scheme
```ts
[
    {
        "character_class_uuid": string,
        "name": string,
        "description": string,
        "hit_die": string,
        "primary_abilities": string[],
        "saving_thow_proficiencies": string[]
    }
]
```
<a id="classes-update"></a>
### [GET/PUT/DELETE] `/classes/{class-uuid}/`
Endpoint is used to fetch/update/delete a class.
<br />

Payload Schema
```ts
{
    "name": string,
    "description": string,
    "hit_die": string,
    "primary_abilities": string[],
    "saving_thow_proficiencies": string[]
}
```
Response scheme
```ts
{
    "character_class_uuid": string,
    "name": string,
    "description": string,
    "hit_die": string,
    "primary_abilities": string[],
    "saving_thow_proficiencies": string[]
}
```
<a id="items"></a>
### [GET/POST] `/items/`
Endpoint is used to fetch/create a item(s).
<br />

`name` is required all other fields are optional. <br />
`treasure_grade` has these choices available (defaults to `normal`): <br />
```python
(
    ("none", "none"),
    ("common", "common"),
    ("uncommon", "uncommon"),
    ("rare", "rare"),
    ("very rare", "very rare"),
    ("legendary", "legendary"),
    ("artifact", "artifact"),
)
```
`treasure_type` has these choices available (defaults to `common`): <br />
```python
(
    ("equipment", "equipment"),
    ("magic", "magic"),
    ("gem", "gem"),
    ("jewelry", "jewelry"),
    ("art", "art"),
    ("trade goods", "trade goods"),
)
```
`currency_denomination` has these choices available (defaults to `gold`): <br />
```python
(
    ("copper", "copper"),
    ("silver", "silver"),
    ("electrum", "electrum"),
    ("gold", "gold"),
    ("platinum", "platinum"),
)
```

Payload Schema
```ts
{
    "name": string,
    "description": string,
    "treasure_grade": string,
    "treasure_type": string,
    "cost": number | null,
    "currency_denomination": string,
    "weight": number
}
```
Response scheme
```ts
[
    {
        "item_uuid": string,
        "name": string,
        "description": string,
        "treasure_grade": string,
        "treasure_type": string,
        "cost": number | null,
        "currency_denomination": string,
        "weight": number
    }
]
```
<a id="items-update"></a>
### [GET/PUT/DELETE] `/items/{item-uuid}/`
Endpoint is used to fetch/update/delete a item.
<br />

Payload Schema
```ts
{
    "name": string,
    "description": string,
    "treasure_grade": string,
    "treasure_type": string,
    "cost": number | null,
    "currency_denomination": string,
    "weight": number
}
```
Response scheme
```ts
[
    {
        "item_uuid": string,
        "name": string,
        "description": string,
        "treasure_grade": string,
        "treasure_type": string,
        "cost": number | null,
        "currency_denomination": string,
        "weight": number
    }
]
```
<a id="weapons"></a>
### [GET/POST] `/items/weapons/`
Endpoint is used to fetch/create a item:weapon.
<br />

`name` is required all other fields are optional. <br />

**Below are weaopn specific items**
`damage_die` has these choices available (defaults to `d6`): <br />
```python
(
    ("d4", "d4"),
    ("d6", "d6"),
    ("d8", "d8"),
    ("d10", "d10"),
    ("d12", "d12"),
    ("d20", "d20"),
)
```
`damage_type` has these choices available (defaults to `null`): <br />
```python
(
    ("bludgeoning", "bludgeoning"),
    ("piercing", "piercing"),
    ("slashing", "slashing"),
    ("magic", "magic"),
    ("acid", "acid"),
    ("cold", "cold"),
    ("fire", "fire"),
    ("force", "force"),
    ("lightning", "lightning"),
    ("necrotic", "necrotic"),
    ("poison", "poison"),
    ("psychic", "psychic"),
    ("radiant", "radiant"),
    ("thunder", "thunder"),
)
```
`is_ranged` defaults to `false` <br />
`weapon_type`defaults to `simple` <br />
`weapon_type` has these choices available (defaults to `simple`): <br />
```python
(
    ("simple", "simple"),
    ("martial", "martial"),
)
```
`weapon_properties` has these choices available (defaults to `null`): <br />
```python
(
    ("ammunition", "ammunition"),
    ("finesse", "finesse"),
    ("light", "light"),
    ("heavy", "heavy"),
    ("loading", "loading"),
    ("range", "range"),
    ("reach", "reach"),
    ("special", "special"),
    ("thrown", "thrown"),
    ("two-handed", "two-handed"),
    ("one-handed", "one-handed"),
    ("versatile", "versatile"),
)

```

Payload Schema
```ts
{
    "name": string,
    "description": string,
    "treasure_grade": string,
    "treasure_type": string,
    "cost": number | null,
    "currency_denomination": string,
    "weight": number,
    "damage_die": string,
    "number_of_die": number,
    "damage_type": string[] | null,
    "is_ranged": boolean,
    "weapon_type": string,
    "weapon_properties": string[] | null,
    "min_range": number | null,
    "max_range": number | null
}
```
Response scheme
```ts
[
    {
        "item_uuid": string,
        "name": string,
        "description": string,
        "treasure_grade": string,
        "treasure_type": string,
        "cost": number | null,
        "currency_denomination": string,
        "weight": number,
        "damage_die": string,
        "number_of_die": number,
        "damage_type": string[] | null,
        "is_ranged": boolean,
        "weapon_type": string,
        "weapon_properties": string[] | null,
        "min_range": number | null,
        "max_range": number | null
    }
]
```
<a id="weapons-update"></a>
### [GET/PUT/DELETE] `/items/weapons/{item-uuid}/`
Endpoint is used to fetch/update/delete a item:weapon.
<br />

Payload Schema
```ts
{
    "name": string,
    "description": string,
    "treasure_grade": string,
    "treasure_type": string,
    "cost": number | null,
    "currency_denomination": string,
    "weight": number,
    "damage_die": string,
    "number_of_die": number,
    "damage_type": string[] | null,
    "is_ranged": boolean,
    "weapon_type": string,
    "weapon_properties": string[] | null,
    "min_range": number | null,
    "max_range": number | null
}
```
Response scheme
```ts
{
    "item_uuid": string,
    "name": string,
    "description": string,
    "treasure_grade": string,
    "treasure_type": string,
    "cost": number | null,
    "currency_denomination": string,
    "weight": number,
    "damage_die": string,
    "number_of_die": number,
    "damage_type": string[] | null,
    "is_ranged": boolean,
    "weapon_type": string,
    "weapon_properties": string[] | null,
    "min_range": number | null,
    "max_range": number | null
}
```



<a id="environments"></a>
# Environment Setup
## TBD rewrite
Windows: <br />
https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows/ <br />
Install pip <br />
`python -m pip install pipenv` <br />

Create virtual environment <br />
`python -m venv venv` <br />

install requirements <br />
`pipenv install` <br />

run env <br />
`source venv/Scripts/activate` <br />
or <br />
`pipenv run activate` <br />
or <br />
`pipenv shell` <br />

Create a django project <br />
`django-admin startproject <mysite>` <br />

Cd to `<mysite>` and run `python manage.py runserver 8000` to start the server <br />

Postgres
- install postgres
- `pip3 install psycopg2`
- add db connection info to settings

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

To create a superuser on said db <br />
`python manage.py createsuperuser` <br />

Create a new folder to house individual apps. <br />
`python manage.py startapp <app_name>` <br />


Adding rest_framework <br />
`'rest_framework'` to installed apps in settings <br />

Add auth and permissions to settings file <br />

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}
```

Running the python backend <br />
`python backend/manage.py runserver 8000` <br />

creating new apps <br />
`python manage.py startapp appName` <br />

Migrate new model changes <br />
`python backend/manage.py makemigrations` <br />
`python backend/manage.py migrate` <br />

To bulk load/dump data <br />
`python manage.py loaddata ./json_data/{json_to_load}.json` <br />
`python manage.py dumpdata {app_name.model_name} > ./json_data/{model_name}.json` <br />

