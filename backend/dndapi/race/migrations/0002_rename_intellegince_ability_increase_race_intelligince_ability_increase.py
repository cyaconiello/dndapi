# Generated by Django 4.0.3 on 2022-03-09 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='race',
            old_name='intellegince_ability_increase',
            new_name='intelligince_ability_increase',
        ),
    ]