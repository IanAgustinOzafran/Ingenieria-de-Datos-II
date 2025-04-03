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
    {"artista": "Adele", "album": "21", "genero": "Pop"}
    {"artista": "John Coltrane", "album": "A Love Supreme", "genero": "Jazz"},
    {"artista": "Pink Floyd", "album": "The Dark Side of the Moon", "genero": "Rock"},
    {"artista": "Billie Holiday", "album": "Lady in Satin", "genero": "Jazz"},
    {"artista": "Ed Sheeran", "album": "Divide", "genero": "Pop"},
])

for musica in musica_collection.find():
    print(musica)
    
for musica in musica_collection.find({"genero": "Rock"}):
    print(musica)