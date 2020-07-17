from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from .Author import Author
from .Shelf import Shelf

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    titleShort = models.CharField(max_length=50, blank=True, null=True)
    author = models.ManyToManyField(Author, null=True, related_name='authors')
    isbn = models.CharField('ISBN', max_length=50, blank=True, null=True)
    zoteroId = models.CharField(max_length=50, blank=True, null=True)
    callNumber = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=50, blank=True, null=True)
    publisherPlace = models.CharField(max_length=50, blank=True, null=True)
    issued = models.IntegerField(blank=True, null=True)
    collectionTitle = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    abstract = models.CharField(max_length=2000, blank=True, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.DO_NOTHING, null=True)


    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])