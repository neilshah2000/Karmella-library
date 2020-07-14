from catalog.models import Shelf
from catalog.serializers.shelfSerializer import ShelfSerializer
from rest_framework_bulk import BulkModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class ShelfViewSet(BulkModelViewSet):
    """
    API endpoint that allows shelves to be viewed or edited.
    """
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    filter_backends = [DjangoFilterBackend]