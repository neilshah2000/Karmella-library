from catalog.models import BookInstance
from users.models import User
from catalog.serializers.bookInstanceSerializer import BookInstanceSerializer
from rest_framework_bulk import BulkModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
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


    @action(detail=False, methods=['post'])
    def checkoutBulk(self, request):
        print(request.user)
        queryset = BookInstance.objects.all()
        updatedBookInstances = []
        for instance in request.data:
            bookInstance = get_object_or_404(queryset, id=instance['id'])
            # make sure book is not already on loan
            # if bookInstance.status == dict(BookInstance.LOAN_STATUS).get('o'):
            if bookInstance.status == 'o':
                content = {'status': 'book already on loan'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            # bookInstance.status = dict(BookInstance.LOAN_STATUS).get('o')
            bookInstance.status = 'o'
            bookInstance.borrower = request.user
            updatedBookInstances.append(bookInstance)
        # if everything is ok, save all now
        for book in updatedBookInstances:
            book.save()
        serializer = BookInstanceSerializer(updatedBookInstances, many=True)
        return Response(serializer.data)

        
    @action(detail=True, methods=['post'])
    def checkin(self, request, pk=None):
        user = request.user.id
        print(request.user)
        queryset = BookInstance.objects.all()
        bookInstance = get_object_or_404(queryset, pk=pk)
        bookInstance.status = dict(BookInstance.LOAN_STATUS).get('a')
        bookInstance.user = None
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


    @action(detail=False, methods=['get'])
    def currentLoans(self, request, pk=None):
        user = request.user.id
        print(request.user)
        myBorrowed = BookInstance.objects.filter(borrower=request.user.id)
        print(myBorrowed)
        serializer = BookInstanceSerializer(myBorrowed, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['post'])
    def returnBook(self, request, pk=None):
        user = request.user.id
        print(request.user)
        queryset = BookInstance.objects.all()
        bookInstance = get_object_or_404(queryset, pk=pk)
        # make sure this user already has the book out on loan
        if bookInstance.status != 'o' or bookInstance.borrower.id != request.user.id:
            content = {'status': 'you have not borrowed this book on the system'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        bookInstance.status = 'a'
        bookInstance.borrower = None
        bookInstance.save()
        serializer = BookInstanceSerializer(bookInstance)
        return Response(serializer.data)