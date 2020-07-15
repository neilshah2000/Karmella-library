import requests
import json
from helpers import loginUser, addAuthor, addAuthorBulk, getAuthorSet


# serverUrl = 'http://127.0.0.1:8000/'
serverUrl = 'https://blooming-mountain-86004.herokuapp.com/'

json_file = '/home/neil/Code/library/locallibrary/data/Karmelako_liburutegia.json'

authorSet = getAuthorSet(json_file)
authList = list()

for authTup in authorSet:
    authDict = dict()
    authDict['first_name'] = authTup[0]
    authDict['last_name'] = authTup[1]
    authList.append(authDict)

response = addAuthorBulk(authList, serverUrl)
print(response.json())
