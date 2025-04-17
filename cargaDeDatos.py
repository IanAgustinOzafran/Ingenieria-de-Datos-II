from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
 
db = client["TPO"]
 
musica_collection = db["Musica"]

with open('musica.json', 'r') as file:
    data = json.load(file)
    musica_collection.insert_many(data)
    file.close()