# Generated by Django 4.0.3 on 2022-03-09 23:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0002_race_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='race_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
