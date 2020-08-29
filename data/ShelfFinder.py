import requests
import json


class ShelfFinder:
    def __init__(self, serverUrl, token):
        self.serverUrl = serverUrl

        url = serverUrl + 'catalog/api/shelves/'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
        }
        response = requests.get(url, headers=headers)
        self.shelves = response.json()

    def getShelves(self):
        return self.shelves

    def findShelf(self, name):
        shelf = next((item for item in self.shelves if (item['name'] == name)), None)
        return shelf
