# Generated by Django 4.0.3 on 2022-03-09 23:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0005_remove_race_languages_race_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='languages',
        ),
        migrations.AddField(
            model_name='race',
            name='languages',
            field=models.CharField(blank=True, choices=[(uuid.UUID('58ab4087-ae49-459e-87ca-02db24379628'), 'Elven'), (uuid.UUID('87af550b-bbff-48d4-b857-f3efe1392d54'), 'Dwarven')], max_length=10),
        ),
    ]