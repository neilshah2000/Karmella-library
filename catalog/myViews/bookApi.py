from catalog.models import Book
from catalog.serializers.bookSerializer import BookSerializer
from rest_framework_bulk import BulkModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class BookViewSet(BulkModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['pages', 'place']
    search_fields = ['title', 'abstract']
