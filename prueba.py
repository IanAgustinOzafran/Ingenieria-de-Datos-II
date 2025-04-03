from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
 
db = client["TPO"]

#db.create_collection("Musica")

for db_name in client.list_database_names():
    print(f"Base de datos: {db_name}")
 
musica_collection = db["Musica"]

musica_collection.insert_many([
    {"artista": "Queen", "album": "A Night at the Opera", "genero": "Rock"},
    {"artista": "The Beatles", "album": "Abbey Road", "genero": "Rock"},
    {"artista": "Miles Davis", "album": "Kind of Blue", "genero": "Jazz"},
    {"artista": "Billie Eilish", "album": "When We All Fall Asleep, Where Do We Go?", "genero": "Pop"},
    {"artista": "Taylor Swift", "album": "1989", "genero": "Pop"},
    {"artista": "Nirvana", "album": "Nevermind", "genero": "Rock"},
    {"artista": "Dua Lipa", "album": "Future Nostalgia", "genero": "Pop"},
    {"artista": "Miles Davis", "album": "Bitches Brew", "genero": "Jazz"},
    {"artista": "Led Zeppelin", "album": "IV", "genero": "Rock"},
    {"artista": "Adele", "album": "21", "genero": "Pop"},
    {"artista": "John Coltrane", "album": "A Love Supreme", "genero": "Jazz"},
    {"artista": "Pink Floyd", "album": "The Dark Side of the Moon", "genero": "Rock"},
    {"artista": "Billie Holiday", "album": "Lady in Satin", "genero": "Jazz"},
    {"artista": "Ed Sheeran", "album": "Divide", "genero": "Pop"},
])

for musica in musica_collection.find():
    print(musica)
    
for musica in musica_collection.find({"genero": "Rock"}):
    print(musica)

    # Filtrar por artista específico
    for musica in musica_collection.find({"artista": "Miles Davis"}):
        print(musica)

    # Filtrar por álbum que contiene una palabra específica
    for musica in musica_collection.find({"album": {"$regex": "Blue"}}):
        print(musica)

    # Filtrar por género y ordenar alfabéticamente por álbum
    for musica in musica_collection.find({"genero": "Pop"}).sort("album", 1):
        print(musica)

    # Filtrar por género y excluir un campo específico en la salida
    for musica in musica_collection.find({"genero": "Jazz"}, {"_id": 0}):
        print(musica)

    # Filtrar por múltiples géneros
    for musica in musica_collection.find({"genero": {"$in": ["Rock", "Jazz"]}}):
        print(musica)

    # Filtrar por álbumes que no pertenecen a un género específico
    for musica in musica_collection.find({"genero": {"$ne": "Pop"}}):
        print(musica)

    # Filtrar por artistas con más de un álbum en la colección
    pipeline = [
        {"$group": {"_id": "$artista", "count": {"$sum": 1}}},
        {"$match": {"count": {"$gt": 1}}}
    ]
    for result in musica_collection.aggregate(pipeline):
        print(result)
