from catalog.models import BookInstance, Book
from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

class BookInstanceSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    book = serializers.StringRelatedField(many=False)
    class Meta:
        model = BookInstance
        list_serializer_class = BulkListSerializer
        fields = '__all__'