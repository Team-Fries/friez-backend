# Generated by Django 4.2 on 2023-04-21 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0011_merge_0010_remove_animal_image_animalimage_0010_trade'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
