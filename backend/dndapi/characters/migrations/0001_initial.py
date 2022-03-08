# Generated by Django 4.0.3 on 2022-03-07 02:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("race", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "character_uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("age", models.PositiveIntegerField(default=1)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "male"), ("female", "female")],
                        default="male",
                        max_length=6,
                    ),
                ),
                ("background", models.TextField(blank=True)),
                (
                    "base_strength",
                    models.PositiveIntegerField(default=13, editable=False),
                ),
                (
                    "base_dexterity",
                    models.PositiveIntegerField(default=16, editable=False),
                ),
                (
                    "base_constitution",
                    models.PositiveIntegerField(default=17, editable=False),
                ),
                (
                    "base_intelligence",
                    models.PositiveIntegerField(default=14, editable=False),
                ),
                ("base_wisdom", models.PositiveIntegerField(default=9, editable=False)),
                (
                    "base_charisma",
                    models.PositiveIntegerField(default=10, editable=False),
                ),
                (
                    "race_uuid",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="race.race",
                    ),
                ),
            ],
        ),
    ]
