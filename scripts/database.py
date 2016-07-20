from transport.models import *
import csv

""" This script can be tested in Django with ipython:
        python manage.py shell
        %run scripts/database.py

    Then save the data file in csv, ideally in data.
"""


def upload_machines_csv(f='../data/transport_machine.csv'):

    with open(f) as fh:
        reader = csv.reader(fh)
        next(reader, None) # Remove header
        for row in reader:
            _, _ = Machine.objects.get_or_create(
                        kind = row[0],
                        brand = row[1],
                        model = row[2],
                        weight = row[3],
                        length = row[4],
                        height = row[5],
                        width = row[6],
                        comment = row[7]
            )
