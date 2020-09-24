import requests
import json
from helpers import loginUser, addShelves

serverUrl = 'http://127.0.0.1:8000/'
# serverUrl = 'https://blooming-mountain-86004.herokuapp.com/'
email = 'neilshahlimited@hotmail.com'
password = 'aslkdflk908'



shelves = [
    {'name': 'Aldizkariak'},
    {'name': 'Biografiak'},
    {'name': 'Haur eta Gazte Literatura'},
    {'name': 'Inperialismoa eta Kolonialismoa'},
    {'name': 'Marxismoa eta Komunismoa'},
    {'name': 'Anarkismoa'}, {'name': 'Borroka Armatua'},
    {'name': 'Herri Indigenak'},
    {'name': 'Kartzela'},
    {'name': 'Musika eta Zinema'},
    {'name': 'Antiespezismoa'},
    {'name': 'Diktadurak'},
    {'name': 'Herri Mugimenduak (Orokorra)Kazetaritza'},
    {'name': 'Narrazioak'},
    {'name': 'Antzerkia'},
    {'name': 'Eleberriak'},
    {'name': 'Hezkuntza'},
    {'name': 'Komikiak'},
    {'name': 'Pentsamendu Kritikoa'},
    {'name': 'Argazkilaritza'},
    {'name': 'Estatuaren Bortxa'},
    {'name': 'Historia'},
    {'name': 'Kritika Literarioa'},
    {'name': 'Poesia'},
    {'name': 'Arraza'},
    {'name': 'Feminismoa'},
    {'name': 'Hiztegiak eta Eskuliburuak'},
    {'name': 'Kritika Politikoa'},
    {'name': 'Urtekariak'},
    {'name': 'Arte Ederrak'},
    {'name': 'Filosofia'},
    {'name': 'Independentismoa'},
    {'name': 'Langile Mugimendua'}
]

token = loginUser({'email': email, 'password': password}, serverUrl)
response = addShelves(shelves, serverUrl, token)
print(response.json())
