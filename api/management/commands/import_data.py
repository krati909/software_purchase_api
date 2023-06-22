import csv
from django.core.management.base import BaseCommand
from api.models import Purchase

class Command(BaseCommand):
    help = 'Import data from CSV'

    def handle(self, *args, **options):
        with open('data.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Purchase.objects.create(
                    item=row['software'],
                    department=row['department'],
                    quantity=int(row['seats']),
                    price=float(row['amount']),
                    transaction_date=row['date']
                )
