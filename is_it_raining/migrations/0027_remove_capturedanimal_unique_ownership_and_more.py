# Generated by Django 4.2 on 2023-04-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0026_capturedanimal_unique_ownership'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='capturedanimal',
            name='unique_ownership',
        ),
    ]
