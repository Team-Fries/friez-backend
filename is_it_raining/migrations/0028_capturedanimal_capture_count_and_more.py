# Generated by Django 4.2 on 2023-04-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0027_capturedanimal_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='capturedanimal',
            name='capture_count',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='capturedanimal',
            name='captured_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='capturedanimal',
            name='last_capture_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='capturedanimal',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
