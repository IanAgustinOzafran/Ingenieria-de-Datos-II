from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
 
db = client["TPO"]
 
musica_collection = db["Musica"]

with open('musica.json', 'r') as file:
    data = json.load(file)
    for musica in data:
        print(f"Artista: {musica['artista']}, Álbum: {musica['album']}, Genero: {musica['genero']}")

