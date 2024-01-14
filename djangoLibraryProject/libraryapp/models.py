from django.db import models
from faker import Faker
import random
# Create your models here.

class Library(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    publisher = models.CharField(max_length=255, verbose_name='publisher')
    author = models.CharField(max_length=255, verbose_name='author')
    title = models.CharField(max_length=255, verbose_name='title')
    page_count = models.IntegerField(default=10, verbose_name='Page Count')
    category = models.CharField(max_length=50, verbose_name='category')
    shelf_location = models.CharField(max_length=50, verbose_name='shelflocation')
    published_date = models.DateField( verbose_name='published date')
    is_in_stock = models.BooleanField(default=True, verbose_name='is in stock')
    date_checked_out = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.title} {self.published_date}"
    
    class Meta:
      db_table = "library"
      verbose_name = 'Library'
      verbose_name_plural = 'Library'

    @staticmethod
    def populate_library_data():
    
        if Library.objects.all().count() >= 200:
            return 
        fake = Faker()
        for _ in range(200):
            Library.objects.create(
                publisher=fake.company()[:50],
                author=fake.name()[:50],
                title=fake.catch_phrase()[:100],
                page_count=random.randint(50, 500),
                category=fake.word()[:50],
                shelf_location=fake.random_element(elements=('A1', 'B2', 'C3')),
                published_date=fake.date_between(start_date='-5y', end_date='today'),
                is_in_stock=random.choice([True, False]),
                date_checked_out=fake.date_between(start_date='-1y', end_date='today') if random.choice([True, False]) else None,
            )