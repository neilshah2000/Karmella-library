from catalog.models import Author
from catalog.serializers.authorSerializer import AuthorSerializer
from rest_framework_bulk import BulkModelViewSet


class AuthorViewSet(BulkModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer