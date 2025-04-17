from pymongo import MongoClient

#Para poder instalar faker
#   pip install pymongo faker
from faker import Faker
import random

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['TPO']
musica_collection = db["Musica"]

# Limpiar la colección antes de insertar nuevos datos (opcional)
#musica_collection.delete_many({})

# Inicializar Faker
fake = Faker()
generos_musicales = ['Rock', 'Pop', 'Jazz', 'Reggaeton', 'Hip-Hop', 'Clásica', 'Electrónica', 'Indie', 'Trap', 'Funk']

# Generar artistas
def generar_artistas(cantidad):
    artistas = []
    for i in range(cantidad):
        artista = {
            'nombre': fake.first_name(),
            'apellido': fake.last_name(),
            'pais_origen': fake.country(),
        }
        artistas.append(artista)
    return artistas

# Generar un álbum asociado a un artista dado
def generar_album(artista):
    return {
        'titulo': fake.sentence(nb_words=random.randint(1,4)).replace('.', ''),
        'anio_lanzamiento': random.randint(1980, 2024),
        'genero': random.choice(generos_musicales),
        'artista': artista
    }
    
# Insertar álbumes
def insertar_albumes_por_artistas(num_artistas=10, num_albumes=4):
    artistas = generar_artistas(num_artistas)
    albumes = []

    for i in range(num_albumes):
        album = generar_album(random.choice(artistas))
        albumes.append(album)

    resultado = musica_collection.insert_many(albumes)
    print(f"Insertados {len(resultado.inserted_ids)} álbumes de {num_artistas} artistas.")
    



# Ejecutar
insertar_albumes_por_artistas(10, 20)  # 10 artistas, 20 álbumes 