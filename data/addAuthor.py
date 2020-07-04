import requests
import json
from helpers import loginUser, addAuthor, addAuthorBulk
from extractAuthors import getAuthorSet


authorSet = getAuthorSet()
authList = list()

for authTup in authorSet:
    authDict = dict()
    authDict['first_name'] = authTup[0]
    authDict['last_name'] = authTup[1]
    authList.append(authDict)

response = addAuthorBulk(authList)
print(response.json())
