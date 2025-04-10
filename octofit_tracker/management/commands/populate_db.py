# Import necessary modules
from django.core.management.base import BaseCommand
from octofit_tracker.models import YourModel  # Replace with your actual model

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Example test data
        test_data = [
            YourModel(field1='Value1', field2='Value2'),  # Replace with actual fields
            YourModel(field1='Value3', field2='Value4'),
        ]

        # Bulk create test data
        YourModel.objects.bulk_create(test_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))