# Generated by Django 5.0.4 on 2024-05-05 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpm', '0004_remove_pet_species'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wpm.owner'),
        ),
    ]
