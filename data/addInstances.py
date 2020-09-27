import requests
import json
import os
from BookInstanceCreator import BookInstanceCreator
from helpers import loginUser, returnBookInstancesFromZoteroJson, addBookInstance

serverUrl = 'http://127.0.0.1:8000/'
# serverUrl = 'https://blooming-mountain-86004.herokuapp.com/'
email = 'neilshahlimited@hotmail.com'
password = 'jkasj703jdkj'

token = loginUser({'email': email, 'password': password}, serverUrl)

zoteroAllBooksFile = '/home/neil/Code/library/locallibrary/data/Karmelako_liburutegia.json'

instancesAndErrors = returnBookInstancesFromZoteroJson(serverUrl, token, zoteroAllBooksFile)
instances = instancesAndErrors['instances']
errors = instancesAndErrors['errors']

# print(instances)
# print(errors)


for inst in instances:
    response = addBookInstance(inst, serverUrl, token)
    print(response.json())