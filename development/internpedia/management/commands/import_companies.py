from internpedia.models import Company
import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import companies data onto database'

    def handle(self, *args, **options):

        for row in csv.DictReader(open('./swe_companies.csv')):
            company = Company(
                    title=row['title'],
                    company_logo=row['logo'],
                    industry=row['industry'],
                    description=row['description'],
                    website=row['website'],
                    )
            company.save()


        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV'))