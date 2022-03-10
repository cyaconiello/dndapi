# Generated by Django 4.0.3 on 2022-03-09 23:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_alter_language_language_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='id',
        ),
        migrations.AlterField(
            model_name='language',
            name='language_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]