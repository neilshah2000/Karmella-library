import requests
import json


class AuthorFinder:
    def __init__(self, serverUrl, token):
        self.serverUrl = serverUrl

        url = serverUrl + 'catalog/api/authors/'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
        }
        response = requests.get(url, headers=headers)
        self.authors = response.json()

    def getAuthors(self):
        return self.authors

    def findAuthor(self, firstName, lastName):
        author = next((item for item in self.authors if (item['first_name'] == firstName and item['last_name'] == lastName)), None)
        return author
