import requests
import json
from helpers import addBooks
from BookCreator import BookCreator

json_file = '/home/neil/Code/library/locallibrary/data/Karmelako_liburutegia.json'

with open(json_file) as json_data:
    library = json.load(json_data)

bc = BookCreator()

books = [
    {
		"id": "http://zotero.org/groups/2204707/items/CCCUZZLR",
		"type": "book",
		"call-number": "329.borr ADA ant",
		"event-place": "Tafalla",
		"ISBN": "978-84-8136-061-5",
		"language": "es",
		"number-of-pages": "354",
		"publisher": "Txalaparta",
		"publisher-place": "Tafalla",
		"title": "Antes del amanecer: una autobiografía",
		"title-short": "Antes del amanecer",
		"author": [
			{
				"family": "Adams",
				"given": "Gerry"
			}
		],
		"issued": {
			"date-parts": [
				[
					"1997"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/groups/2204707/items/US8B7U3X",
		"type": "book",
		"call-number": "329.borr ADA ant",
		"event-place": "Tafalla",
		"ISBN": "978-84-8136-061-5",
		"language": "es",
		"number-of-pages": "354",
		"publisher": "Txalaparta",
		"publisher-place": "Tafalla",
		"title": "Antes del amanecer: una autobiografía",
		"title-short": "Antes del amanecer",
		"author": [
			{
				"family": "Adams",
				"given": "Gerry"
			}
		],
		"issued": {
			"date-parts": [
				[
					"1997"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/groups/2204707/items/Z27ZMN7U",
		"type": "book",
		"call-number": "329.borr ADA hac",
		"collection-title": "Belen Gonzalez Peñalbaren Kolekzioa",
		"event-place": "Tafalla",
		"ISBN": "978-84-86597-34-4",
		"language": "es",
		"number-of-pages": "240",
		"publisher": "Txalaparta",
		"publisher-place": "Tafalla",
		"title": "Hacia la libertad de Irlanda",
		"author": [
			{
				"family": "Adams",
				"given": "Gerry"
			}
		],
		"issued": {
			"date-parts": [
				[
					"1991"
				]
			]
		}
	}
]

createdBooks = []
isbnSet = set()
for book in library:
    created = bc.createBook(book)
    createdBooks.append(created)
    unq = (created.get('isbn'), created.get('title'))
    isbnSet.add(unq)
    # response = addBooks(created)
    # print(response.json())

for dat in isbnSet:
    print(dat)

print(len(library))
print(len(isbnSet))