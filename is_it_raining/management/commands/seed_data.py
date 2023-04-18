from django.core.management.base import BaseCommand, CommandError

from is_it_raining.models import Animal, Weather
from config import settings


class Command(BaseCommand):
    help = "Create some data for development"

    def handle(self, *args, **options):
        if settings.DEBUG:

            animal_data = [
                {
                    "name": "Alligator",
                    "weather_code": 2
                },
                {
                    "name": "Toad",
                    "weather_code": 3
                },
                {
                    "name": "Megalodon",
                    "weather_code": 5
                },
                {
                    "name": "Goat",
                    "weather_code": 6
                },
                {
                    "name": "Trex",
                    "weather_code": 7
                },
                {
                    "name": "Toucan",
                    "weather_code": 8
                },
                {
                    "name": "Stegosaurus",
                    "weather_code": 8
                }
            ]

            for animal in animal_data:
                weather_code = animal['weather_code']

                weather, created = Weather.objects.get_or_create(
                    weather_code=weather_code)

                Animal.objects.get_or_create(
                    name=animal["name"],
                    weather=weather
                )

            self.stdout.write(self.style.SUCCESS("Objects added to database."))

        else:
            raise CommandError(
                "This command only runs when DEBUG is set to True.")
