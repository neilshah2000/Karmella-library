import json

def getAuthorSet():

    json_file = '/home/neil/Code/library/locallibrary/data/Karmelako_liburutegia.json'

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

    # t = getAuthorTupleList(library[1])

    # print(t)

    for book in library:
        if 'author' in book:
            authorList = getAuthorTupleList(book)
            for author in authorList:
                authors.add(author)

    return authors
