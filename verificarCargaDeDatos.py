from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
 
db = client["TPO"]
 
musica_collection = db["Musica"]

# Verificar la inserción
for musica in musica_collection.find():
    print(f"Artista: {musica['artista']['nombre']} {musica['artista']['apellido']}")
    print(f"Álbum: {musica['titulo']}")
    print(f"Año de lanzamiento: {musica['anio_lanzamiento']}")
    print(f"Género: {musica['genero']}")
    print("Canciones:")
    for cancion in musica['canciones']:
        print(f" - {cancion['nombre']} ({cancion['duracion']})")
    print("\n")
# Cerrar la conexión a la base de datos
client.close()

