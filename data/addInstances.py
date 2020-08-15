import requests
import json
import os
from BookInstanceCreator import BookInstanceCreator
from helpers import returnBookInstancesFromZoteroJson, addBookInstance

serverUrl = 'http://127.0.0.1:8000/'
# serverUrl = 'https://blooming-mountain-86004.herokuapp.com/'

zoteroAllBooksFile = '/home/neil/Code/library/locallibrary/data/Karmelako_liburutegia.json'

instancesAndErrors = returnBookInstancesFromZoteroJson(serverUrl, zoteroAllBooksFile)
instances = instancesAndErrors['instances']
errors = instancesAndErrors['errors']

# print(instances)
# print(errors)

for inst in instances:
    response = addBookInstance(inst, serverUrl)
    print(response.json())