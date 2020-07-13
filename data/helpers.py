import requests
import json
from datetime import datetime, timedelta


# serverUrl = 'http://127.0.0.1:8000/'
serverUrl = 'https://blooming-mountain-86004.herokuapp.com/'

# User is object like {'username': 'olga', 'password': 'olga'}
def loginUser(user):
    url = serverUrl + 'authentication/token/'
    response = requests.post(url, data = user)
    json_response = response.json()
    return json_response['access_token']


def addAuthor(firstName, lastName):
    bid = {
        "first_name": firstName,
        "last_name": lastName
    }
    url = serverUrl + 'catalog/api/authors/'
    response = requests.post(url, data = bid)
    return response

def addAuthorBulk(authorList):
    jsonData = json.dumps(authorList)
    url = serverUrl + 'catalog/api/authors/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data = jsonData)
    return response


def addBooks(booksList):
    jsonData = json.dumps(booksList)
    url = serverUrl + 'catalog/api/books/'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data = jsonData)
    return response

