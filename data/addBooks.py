import requests
import json
import os
from helpers import loginUser, addBooks, returnZoteroJsonAsCatalogObjects, getShelfNamesAndFilePaths

serverUrl = 'http://127.0.0.1:8000/'
# serverUrl = 'https://blooming-mountain-86004.herokuapp.com/'
email = 'neilshahlimited@hotmail.com'
password = 'aslkdflk908'


shelfDirectoryPath = '/home/neil/Code/library/locallibrary/data/Zotero Export'

shelfFiles = getShelfNamesAndFilePaths(shelfDirectoryPath)

token = loginUser({'email': email, 'password': password}, serverUrl)

for shelf in shelfFiles:
    books = returnZoteroJsonAsCatalogObjects(shelf['path'], serverUrl, token, shelf['name'])
    
    for book in books:
        # print(book)
        response = addBooks(book, serverUrl, token)
        print(response.json())
