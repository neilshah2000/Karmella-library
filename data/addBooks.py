import requests
import json
import os
from helpers import addBooks, returnZoteroJsonAsCatalogObjects, getShelfNamesAndFilePaths

serverUrl = 'http://127.0.0.1:8000/'
# serverUrl = 'https://blooming-mountain-86004.herokuapp.com/'


shelfDirectoryPath = '/home/neil/Code/library/locallibrary/data/Zotero Export'

shelfFiles = getShelfNamesAndFilePaths(shelfDirectoryPath)

for shelf in shelfFiles:
    books = returnZoteroJsonAsCatalogObjects(shelf['path'], serverUrl, shelf['name'])
    
    for book in books:
        # print(book)
        response = addBooks(book, serverUrl)
        print(response.json())
