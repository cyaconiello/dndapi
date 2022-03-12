# Generated by Django 4.0.3 on 2022-03-10 23:42

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "item_uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=120, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "treasure_grade",
                    models.CharField(
                        choices=[
                            ("none", "none"),
                            ("common", "common"),
                            ("uncommon", "uncommon"),
                            ("rare", "rare"),
                            ("very rare", "very rare"),
                            ("legendary", "legendary"),
                            ("artifact", "artifact"),
                        ],
                        default="normal",
                        max_length=120,
                    ),
                ),
                (
                    "treasure_type",
                    models.CharField(
                        choices=[
                            ("equipment", "equipment"),
                            ("magic", "magic"),
                            ("gem", "gem"),
                            ("jewelry", "jewelry"),
                            ("art", "art"),
                            ("trade goods", "trade goods"),
                        ],
                        default="common",
                        max_length=120,
                    ),
                ),
                ("cost", models.IntegerField(blank=True, null=True)),
                (
                    "currency_denomination",
                    models.CharField(
                        choices=[
                            ("copper", "copper"),
                            ("silver", "silver"),
                            ("electrum", "electrum"),
                            ("gold", "gold"),
                            ("platinum", "platinum"),
                        ],
                        default="gold",
                        max_length=120,
                    ),
                ),
                ("weight", models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Weapon",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="items.item",
                    ),
                ),
                ("is_ranged", models.BooleanField(default=False)),
                (
                    "damage_die",
                    models.CharField(
                        choices=[
                            ("d4", "d4"),
                            ("d6", "d6"),
                            ("d8", "d8"),
                            ("d10", "d10"),
                            ("d12", "d12"),
                            ("d20", "d20"),
                        ],
                        default="d6",
                        max_length=100,
                    ),
                ),
                ("number_of_die", models.PositiveIntegerField(default=1)),
                (
                    "damage_type",
                    multiselectfield.db.fields.MultiSelectField(
                        blank=True,
                        choices=[
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
                        ],
                        max_length=106,
                        null=True,
                    ),
                ),
                (
                    "weapon_type",
                    models.CharField(
                        choices=[("simple", "simple"), ("martial", "martial")],
                        default="simple",
                        max_length=100,
                    ),
                ),
                (
                    "weapon_properties",
                    multiselectfield.db.fields.MultiSelectField(
                        blank=True,
                        choices=[
                            ("ammunition", "ammunition"),
                            ("finesse", "finesse"),
                            ("light", "light"),
                            ("heavy", "heavy"),
                            ("loading", "loading"),
                            ("range", "range"),
                            ("reach", "reach"),
                            ("speacial", "speacial"),
                            ("thrown", "thrown"),
                            ("two-handed", "two-handed"),
                            ("one-handed", "one-handed"),
                            ("versatile", "versatile"),
                        ],
                        max_length=98,
                        null=True,
                    ),
                ),
                ("min_range", models.IntegerField(blank=True, null=True)),
                ("max_range", models.IntegerField(blank=True, null=True)),
            ],
            bases=("items.item",),
        ),
    ]
