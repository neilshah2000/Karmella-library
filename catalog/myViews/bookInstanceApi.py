from catalog.models import BookInstance
from catalog.serializers.bookInstanceSerializer import BookInstanceSerializer
from rest_framework_bulk import BulkModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class BookInstanceViewSet(BulkModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
