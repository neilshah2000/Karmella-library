from AuthorFinder import AuthorFinder

class BookCreator:
    def __init__(self):
        self.authorFinder = AuthorFinder('https://blooming-mountain-86004.herokuapp.com/')
    
    def createBook(self, zoteroBook):
        title = zoteroBook.get('title')
        titleShort = zoteroBook.get('title-short')
        isbn = zoteroBook.get('ISBN')
        zoteroId =  zoteroBook.get('id')
        callNumber = zoteroBook.get('call-number')
        language =  zoteroBook.get('language')
        pages = zoteroBook.get('number-of-pages')
        publisher =  zoteroBook.get('publisher')
        publisherPlace = zoteroBook.get('publisher-place')
        collectionTitle = zoteroBook.get('collection-title')
        place = zoteroBook.get('event-place')
        abstract = zoteroBook.get('abstract')

        issued = self.getIssued(zoteroBook)
        author = self.getAuthors(zoteroBook)

        aBook = {
            'title': title,
            'titleShort': titleShort,
            'isbn': isbn,
            'zoteroId': zoteroId,
            'callNumber': callNumber,
            'language': language,
            'pages': pages,
            'publisher': publisher,
            'publisherPlace': publisherPlace,
            'collectionTitle': collectionTitle,
            'place': place,
            'abstract': abstract,
            'issued': issued,
            'author': author
        }

        return aBook
    
    def getIssued(self, zoteroBook):
        issued = None
        try:
            issued = int(zoteroBook['issued']['date-parts'][0][0])
        except:
            print('No issued')
        finally:
            return issued
    
    def getAuthors(self, zoteroBook):
        authors = []
        try:
            for auth in zoteroBook.get('author'):
                authDict = self.authorFinder.findAuthor(auth.get('given'), auth.get('family'))
                authors.append(authDict.get('id'))
        except Exception as e:
            print(e)
        finally:
            return authors