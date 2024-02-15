from django.db import models

# Create your models here.
class Library(models.Model):
    publisher = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    titlle = models.CharField(max_length=255)
    page_count = models.IntegerField()
    category = models.CharField(max_length=50)
    shelf_location = models.CharField(max_length=20)
    publish_date = models.DateTimeField(auto_now_add=True)
    is_in_stock = models.BooleanField(default=True)
    checked_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.titlle}"