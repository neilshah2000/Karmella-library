import requests
import json


class BookInstanceCreator:
    def __init__(self, serverUrl, token):
        print('calling api...')
        self.serverUrl = serverUrl

        url = serverUrl + 'catalog/api/books/'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
        }
        response = requests.get(url, headers=headers)
        self.books = response.json()
        print('complete')

    def getBooks(self):
        return self.books

    def getBookInstanceObject(self, book):
        foundBook = next((item for item in self.books if (item['title'] == book['title'])), None)
        if foundBook is not None:
            return {
                'book': foundBook['id']
            }
        else:
            raise ValueError('Did not find the book', book)
