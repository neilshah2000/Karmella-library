from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

class BookDetailView(generic.DetailView):
    model = Book