from catalog.models import Author
from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

class AuthorSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Author
        list_serializer_class = BulkListSerializer
        fields = fields = '__all__'