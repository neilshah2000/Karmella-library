from catalog.models import Book
from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

class BookSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Book
        list_serializer_class = BulkListSerializer
        fields = '__all__'