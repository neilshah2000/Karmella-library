from catalog.models import Book
from catalog.models import Author
from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)
from catalog.serializers.authorSerializer import AuthorSerializer
from catalog.serializers.bookInstanceSerializer import BookInstanceSerializer

class BookSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    # author = AuthorSerializer(many=True, read_only=True) # will be read not written

    author = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Author.objects.all())
    author_names = serializers.StringRelatedField(many=True, source='author',read_only=True)
    copies = BookInstanceSerializer(many=True, read_only=True)
    # copies = serializers.ListField()

    class Meta:
        model = Book
        list_serializer_class = BulkListSerializer
        fields = '__all__'