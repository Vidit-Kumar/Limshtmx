# serializers.py
from rest_framework import serializers
from library.models import Library

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id','titlle','author','publisher','category','page_count','shelf_location','publish_date','is_in_stock','checked_out']

class CheckoutSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()