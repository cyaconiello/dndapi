# Generated by Django 4.0.3 on 2022-03-13 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character_classes', '0001_initial'),
        ('characters', '0002_character_character_class_character_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='character_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character_classes.characterclass'),
        ),
    ]
