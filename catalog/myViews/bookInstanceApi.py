from catalog.models import BookInstance
from catalog.serializers.bookInstanceSerializer import BookInstanceSerializer
from rest_framework_bulk import BulkModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

class BookInstanceViewSet(BulkModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        user = request.user.id
        print(request.user)
        queryset = BookInstance.objects.all()
        bookInstance = get_object_or_404(queryset, pk=pk)
        bookInstance.status = dict(BookInstance.LOAN_STATUS).get('o')
        bookInstance.save()
        serializer = BookInstanceSerializer(bookInstance)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def checkin(self, request, pk=None):
        user = request.user.id
        print(request.user)
        queryset = BookInstance.objects.all()
        bookInstance = get_object_or_404(queryset, pk=pk)
        bookInstance.status = dict(BookInstance.LOAN_STATUS).get('a')
        bookInstance.save()
        serializer = BookInstanceSerializer(bookInstance)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def reserve(self, request, pk=None):
        user = request.user.id
        print(request.user)
        queryset = BookInstance.objects.all()
        bookInstance = get_object_or_404(queryset, pk=pk)
        bookInstance.status = dict(BookInstance.LOAN_STATUS).get('r')
        bookInstance.save()
        serializer = BookInstanceSerializer(bookInstance)
        return Response(serializer.data)