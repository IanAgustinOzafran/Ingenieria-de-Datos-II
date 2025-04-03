from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
 
db = client["TPO"]

db.create_collection("Musica")

for db_name in client.list_database_names():
    print(f"Base de datos: {db_name}")
 
musica_collection = db["Musica"]
#insertar musica

for musica in musica_collection.find():
    print(musica)
    
for musica in musica_collection.find({"genero": "Rock"}):
    print(musica)