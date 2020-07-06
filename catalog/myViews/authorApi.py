from catalog.models import Author
from catalog.serializers.authorSerializer import AuthorSerializer
from rest_framework_bulk import BulkModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class AuthorViewSet(BulkModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['first_name', 'last_name']