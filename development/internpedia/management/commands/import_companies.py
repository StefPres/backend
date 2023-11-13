from internpedia.models import Company, Internship
import csv
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import swe internships data onto database'

    def handle(self, *args, **options):

        for row in csv.DictReader(open('./swe_internships.csv')):
            company = Company.objects.get(title=row['company'])
            internship = Internship(
                title=row['title'],
                location=row['location'],
                description=row['description'],
                paid=row['paid'] == 'TRUE'
            )
            internship.company = company

            internship.save()



        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV'))