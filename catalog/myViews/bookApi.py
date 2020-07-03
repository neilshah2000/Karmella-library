from catalog.models import Book
from catalog.serializers.bookSerializer import BookSerializer
from rest_framework_bulk import BulkModelViewSet

class BookViewSet(BulkModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer