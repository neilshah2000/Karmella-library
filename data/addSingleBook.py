import requests
import json
import os
from helpers import addBooks, returnZoteroJsonAsCatalogObjects, getShelfNamesAndFilePaths

serverUrl = 'http://127.0.0.1:8000/'
# serverUrl = 'https://blooming-mountain-86004.herokuapp.com/'

book = {
    "id": "http://zotero.org/groups/2204707/items/GAZT5NR2",
    "type": "book",
    "call-number": "329.borr GUE ern",
    "event-place": "La Habana",
    "ISBN": "---",
    "language": "es",
    "number-of-pages": "698",
    "number-of-volumes": "2",
    "publisher": "Casa de las Americas",
    "publisher-place": "La Habana",
    "title": "Ernesto Che Guevara obras, 1957-1967: La accion armada",
    "volume": "2",
    "author": [
        {
            "family": "Guevara",
            "given": "Ernesto (Che)"
        }
    ],
    "issued": {
        "date-parts": [
            [
                "1970"
            ]
        ]
    }
}

response = addBooks(book, serverUrl)
print(response.json())
