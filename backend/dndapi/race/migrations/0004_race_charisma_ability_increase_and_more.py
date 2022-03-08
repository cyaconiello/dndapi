# Generated by Django 4.0.3 on 2022-03-07 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("race", "0003_remove_race_sub_class"),
    ]

    operations = [
        migrations.AddField(
            model_name="race",
            name="charisma_ability_increase",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="race",
            name="constitution_ability_increase",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="race",
            name="dexterity_ability_increase",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="race",
            name="intellegince_ability_increase",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="race",
            name="strength_ability_increase",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="race",
            name="wisdom_ability_increase",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
