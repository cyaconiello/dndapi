# Generated by Django 4.0.3 on 2022-03-09 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_alter_character_base_constitution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='base_charisma',
            field=models.PositiveIntegerField(default=12, editable=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='base_constitution',
            field=models.PositiveIntegerField(default=14, editable=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='base_dexterity',
            field=models.PositiveIntegerField(default=15, editable=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='base_intelligence',
            field=models.PositiveIntegerField(default=17, editable=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='base_strength',
            field=models.PositiveIntegerField(default=8, editable=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='base_wisdom',
            field=models.PositiveIntegerField(default=11, editable=False),
        ),
    ]
