from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
 
db = client["TPO"]
 
musica_collection = db["Musica"]

# Verificar la inserción
for musica in musica_collection.find():
    for album in musica:
        print(album)
# Cerrar la conexión a la base de datos
client.close()

