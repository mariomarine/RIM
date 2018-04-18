from django.core.management.base import BaseCommand, CommandError
from rentals.models import Gear
import csv

class Command(BaseCommand):
    help = 'Import Gear from csv'

    def handle(self, *args, **options):
        with open('gps_rental.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                for count in range(0, int(row['Quantity'])):
                    mod =  Gear(
                        # gear_type = row['Type'],
                        gear_type = 'Bike',
                        category = row['Category'],
                        make = row['Make'],
                        model = row['Model'],
                        size = row['Size'],
                        # weight_range = row['Weight range'],
                        color = row['Color'],
                        # description = row['Description'],
                        # note = row['Note'],
                        serial = row['Serial']
                    )
                    mod.save()
