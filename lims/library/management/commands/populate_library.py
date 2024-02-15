import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from library.models import Library
from django.utils import timezone
import datetime

class Command(BaseCommand):

    # Insert data to library if the table is empty

    def handle(self, *args, **options):
        if not Library.objects.exists():
            self.stdout.write('Table is Empty. Inserting random Data...')
            self.insert_library()
            self.stdout.write('Data Insert Successfully...')
        else:
            self.stdout.write('Table in not Empty')
    

    def insert_library(self):
        
        categories = ['Action and adventure', 'Anthology', 'Biography', 'Comic book', 'Historical fiction','Poetry']
        shelf_locations = ['LEVEL-A','LEVEL-B','LEVEL-C','LEVEL-D','LEVEL-E']
        for _ in range(200):
            publisher = self._generate_random_text()
            author = self._generate_random_text()
            titlle = self._generate_random_text()
            page_count = random.randint(100, 1000)
            category = random.choices(categories, k=1)[0]
            shelf_location = random.choices(shelf_locations, k=1)[0]
            publish_date = self._generate_random_date()
            is_in_stock = random.choice([True, False])
            
            Library.objects.create(publisher=publisher, author=author,titlle=titlle,page_count=page_count,
                                   category=category,shelf_location=shelf_location,publish_date=publish_date,
                                   is_in_stock=is_in_stock)
    
    def _generate_random_text(self, length=10):
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(random.choices(characters, k=length))
    
    def _generate_random_date(self):
        start_date = timezone.now() - timezone.timedelta(days=365*10)  # 10 years ago
        end_date = timezone.now()
        random_delta = datetime.timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        return start_date + random_delta