import requests
import json
from helpers import loginUser, addAuthor, addAuthorBulk, getAuthorSet


serverUrl = 'http://127.0.0.1:8000/'
# serverUrl = 'https://blooming-mountain-86004.herokuapp.com/'
email = 'neilshahlimited@hotmail.com'
password = 'aslkdflk908'

json_file = '/home/neil/Code/library/locallibrary/data/Karmelako_liburutegia.json'

authorSet = getAuthorSet(json_file)
authList = list()

for authTup in authorSet:
    authDict = dict()
    authDict['first_name'] = authTup[0]
    authDict['last_name'] = authTup[1]
    authList.append(authDict)

token = loginUser({'email': email, 'password': password}, serverUrl)
response = addAuthorBulk(authList, serverUrl, token)
print(response.json())
