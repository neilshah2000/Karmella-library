import requests
import json
import os
from datetime import datetime, timedelta
from BookCreator import BookCreator
from BookInstanceCreator import BookInstanceCreator


# User is object like {'username': 'olga', 'password': 'olga'}
def loginUser(user, serverUrl):
    url = serverUrl + 'auth/token/login/'
    response = requests.post(url, data = user)
    json_response = response.json()
    return json_response['auth_token']


def addShelves(shelfList, serverUrl, token):
    jsonData = json.dumps(shelfList)
    url = serverUrl + 'catalog/api/shelves/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + token
    }
    response = requests.post(url, headers=headers, data = jsonData)
    return response


def addAuthor(firstName, lastName, serverUrl, token):
    bid = {
        "first_name": firstName,
        "last_name": lastName
    }
    url = serverUrl + 'catalog/api/authors/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + token
    }
    response = requests.post(url, headers=headers, data = bid)
    return response

def addAuthorBulk(authorList, serverUrl, token):
    jsonData = json.dumps(authorList)
    url = serverUrl + 'catalog/api/authors/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + token
    }
    response = requests.post(url, headers=headers, data = jsonData)
    return response


def addBooks(booksList, serverUrl, token):
    jsonData = json.dumps(booksList)
    url = serverUrl + 'catalog/api/books/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + token
    }
    response = requests.post(url, headers=headers, data = jsonData)
    return response

def addBookInstance(bookInstance, serverUrl, token):
    jsonData = json.dumps(bookInstance)
    url = serverUrl + 'catalog/api/copies/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + token
    }
    response = requests.post(url, headers=headers, data = jsonData)
    return response


def returnZoteroJsonAsCatalogObjects(json_file, serverUrl, token, shelfName):
    with open(json_file) as json_data:
        library = json.load(json_data)

    bc = BookCreator(serverUrl, token)

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

def returnBookInstancesFromZoteroJson(serverUrl, token, zoteroFile):
    with open(zoteroFile) as json_data:
        library = json.load(json_data)

    bic = BookInstanceCreator(serverUrl, token)
    errors = []
    bookInstances = []
    for myInst in library:
        try:
            instance = bic.getBookInstanceObject(myInst)
            bookInstances.append(instance)
        except Exception as error:
            # print(error)
            errors.append(error)

    return {
        'instances': bookInstances,
        'errors': errors
    }