import csv
from rentals.models import Gear

filename = input('filename: ')

with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        for count in range(0, row['Quantity']):
            mod =  Gear(
                gear_type = row['Type'],
                catetory = row['Category'],
                make = row['Make'],
                model = row['Model'],
                size = row['Size'],
                weight_range = row['Weight range'],
                color = row['Color'],
                description = row['Description'],
                note = row['Note']
                serial = row['Serial'],
            )
