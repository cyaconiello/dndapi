# Generated by Django 4.0.3 on 2022-03-07 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0006_alter_character_base_charisma_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="base_charisma",
            field=models.PositiveIntegerField(default=12, editable=False),
        ),
        migrations.AlterField(
            model_name="character",
            name="base_intelligence",
            field=models.PositiveIntegerField(default=15, editable=False),
        ),
        migrations.AlterField(
            model_name="character",
            name="base_strength",
            field=models.PositiveIntegerField(default=16, editable=False),
        ),
        migrations.AlterField(
            model_name="character",
            name="base_wisdom",
            field=models.PositiveIntegerField(default=13, editable=False),
        ),
    ]
