import requests
import json


class ShelfFinder:
    def __init__(self, serverUrl):
        self.serverUrl = serverUrl

        url = serverUrl + 'catalog/api/shelves/'
        response = requests.get(url)
        self.shelves = response.json()

    def getShelves(self):
        return self.shelves

    def findShelf(self, name):
        shelf = next((item for item in self.shelves if (item['name'] == name)), None)
        return shelf
