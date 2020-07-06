import requests
import json


class AuthorFinder:
    def __init__(self, serverUrl):
        self.serverUrl = serverUrl

        url = serverUrl + 'catalog/api/authors/'
        response = requests.get(url)
        self.authors = response.json()

    def getAuthors(self):
        return self.authors

    def findAuthor(self, firstName, lastName):
        author = next((item for item in self.authors if (item['first_name'] == firstName and item['last_name'] == lastName)), None)
        return author
