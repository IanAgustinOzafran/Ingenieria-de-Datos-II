from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
 
db = client["TPO"]
 
musica_collection = db["Musica"]

# Eliminar todos los documentos de la colección
musica_collection.delete_many({})
# Cerrar la conexión a la base de datos
client.close()