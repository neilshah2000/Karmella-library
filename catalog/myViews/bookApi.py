from catalog.models import Book
from rest_framework import viewsets
from catalog.serializers.bookSerializer import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer