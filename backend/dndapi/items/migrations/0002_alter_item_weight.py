# Generated by Django 4.0.3 on 2022-03-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]
