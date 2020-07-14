from catalog.models import Shelf
from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

class ShelfSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Shelf
        list_serializer_class = BulkListSerializer
        fields = '__all__'