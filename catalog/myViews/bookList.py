from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2