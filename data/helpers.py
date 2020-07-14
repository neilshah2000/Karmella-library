import requests
import json
import os
from datetime import datetime, timedelta
from BookCreator import BookCreator


# User is object like {'username': 'olga', 'password': 'olga'}
def loginUser(user, serverUrl):
    url = serverUrl + 'authentication/token/'
    response = requests.post(url, data = user)
    json_response = response.json()
    return json_response['access_token']


def addShelves(shelfList, serverUrl):
    jsonData = json.dumps(shelfList)
    url = serverUrl + 'catalog/api/shelves/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data = jsonData)
    return response


def addAuthor(firstName, lastName, serverUrl):
    bid = {
        "first_name": firstName,
        "last_name": lastName
    }
    url = serverUrl + 'catalog/api/authors/'
    response = requests.post(url, data = bid)
    return response

def addAuthorBulk(authorList, serverUrl):
    jsonData = json.dumps(authorList)
    url = serverUrl + 'catalog/api/authors/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data = jsonData)
    return response


def addBooks(booksList, serverUrl):
    jsonData = json.dumps(booksList)
    url = serverUrl + 'catalog/api/books/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data = jsonData)
    return response


def returnZoteroJsonAsCatalogObjects(json_file, serverUrl, shelfName):
    with open(json_file) as json_data:
        library = json.load(json_data)

    bc = BookCreator(serverUrl)

    createdBooks = []
    for book in library:
        created = bc.createBook(book, shelfName)
        createdBooks.append(created)
    
    return createdBooks



def getAuthorSet(json_file):
    with open(json_file) as json_data:
        library = json.load(json_data)

    authors = set()

    def getAuthorTupleList(book):
        first = ''
        last = ''
        authorList = []
        author = book['author'][0]
        for author in book['author']:
            if 'given' in author:
                first = author['given']
            if 'family' in author:
                last = author['family']
            authorList.append((first, last))
        return authorList

    for book in library:
        if 'author' in book:
            authorList = getAuthorTupleList(book)
            for author in authorList:
                authors.add(author)

    return authors

def getShelfNamesAndFilePaths(shelfDirectoryPath):
    shelfFiles = os.listdir(shelfDirectoryPath)
    namesAndPaths = []
    for myFile in shelfFiles:
        shelfName = myFile[:-5]
        shelfFilePath = os.path.join(shelfDirectoryPath, myFile)
        namesAndPaths.append({
            'name': shelfName,
            'path': shelfFilePath
        })
    return namesAndPaths